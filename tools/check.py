#!/usr/bin/env python3
"""Checks the hand-built pages before they go public. Uses only the standard library.

Run from the repo root:  python3 -I tools/check.py

It checks the new pages (index.html, 404.html, the redirect pages) for:
- markup: unclosed or stray tags, duplicate ids;
- links: every local file and #anchor a page points to exists; no http:// links;
- images: alt text, width and height, and the file exists;
- headings: one h1 per page, no skipped levels;
- structured data: the JSON-LD parses;
- agent files: llms.txt and robots.txt exist, and every thesetox.github.io link in llms.txt
  points at a file in this repo.
It exits 1 and lists the problems if anything fails.
"""
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urlparse, unquote
import json
import re
import sys

ROOT = Path(__file__).resolve().parent.parent
# Every page in the site: the home page, the notes page, the 404 page and the redirect pages.
PAGES = sorted(p.name for p in ROOT.glob("*.html"))
VOID = {"area", "base", "br", "col", "embed", "hr", "img", "input", "link", "meta", "source", "track", "wbr"}
SITE = "thesetox.github.io"
# Project sites under thesetox.github.io that other repositories publish.
OTHER_REPOS = ("kmp-sample-diagrams", "commitpath-site", "KMP-Playground-Document", "Prepare")


class Page(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.stack, self.ids, self.links, self.images, self.headings = [], [], [], [], []
        self.problems, self.jsonld, self._in_jsonld = [], [], False

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if tag not in VOID:
            self.stack.append((tag, self.getpos()[0]))
        if "id" in a:
            self.ids.append(a["id"])
        if tag == "a" and "href" in a:
            self.links.append((a["href"], self.getpos()[0]))
        if tag == "link" and a.get("rel") in ("stylesheet", "icon") and "href" in a:
            self.links.append((a["href"], self.getpos()[0]))
        if tag == "img":
            self.images.append((a, self.getpos()[0]))
        if re.fullmatch(r"h[1-6]", tag):
            self.headings.append((int(tag[1]), self.getpos()[0]))
        if tag == "script" and a.get("type") == "application/ld+json":
            self._in_jsonld = True
            self.jsonld.append("")

    def handle_endtag(self, tag):
        if tag in VOID:
            return
        if not self.stack:
            self.problems.append(f"line {self.getpos()[0]}: stray </{tag}>")
            return
        open_tag, line = self.stack.pop()
        if open_tag != tag:
            self.problems.append(f"line {self.getpos()[0]}: </{tag}> closes <{open_tag}> from line {line}")
        if tag == "script":
            self._in_jsonld = False

    def handle_data(self, data):
        if self._in_jsonld:
            self.jsonld[-1] += data


def local_target(page: Path, href: str):
    """Return (file path, anchor) for a link inside this site, or None for outside links."""
    u = urlparse(href)
    if u.scheme in ("mailto", "tel"):
        return None
    if u.scheme in ("http", "https"):
        if u.netloc != SITE or u.path.lstrip("/").startswith(OTHER_REPOS):
            return None
        path = u.path
    elif u.scheme:
        return None
    else:
        path = u.path
    if path.startswith("/"):
        target = ROOT / unquote(path.lstrip("/"))
    elif path:
        target = page.parent / unquote(path)
    else:
        target = page
    if target.is_dir() or str(path).endswith("/"):
        target = target / "index.html"
    return target, u.fragment


def check_page(name: str, problems: list, anchors_cache: dict):
    page = ROOT / name
    if not page.exists():
        problems.append(f"{name}: missing")
        return
    p = Page()
    p.feed(page.read_text(encoding="utf-8"))
    p.close()
    problems += [f"{name}: {x}" for x in p.problems]
    for tag, line in p.stack:
        problems.append(f"{name}: <{tag}> from line {line} is never closed")
    dupes = {i for i in p.ids if p.ids.count(i) > 1}
    for d in sorted(dupes):
        problems.append(f"{name}: duplicate id \"{d}\"")
    anchors_cache[page] = set(p.ids)

    for href, line in p.links:
        if href.startswith("http://"):
            problems.append(f"{name} line {line}: insecure link {href}")
        t = local_target(page, href)
        if not t:
            continue
        target, anchor = t
        if not target.exists():
            problems.append(f"{name} line {line}: {href} points at a missing file")
            continue
        if anchor and target.suffix == ".html":
            if target not in anchors_cache:
                q = Page()
                q.feed(target.read_text(encoding="utf-8", errors="replace"))
                anchors_cache[target] = set(q.ids)
            if anchor not in anchors_cache[target]:
                problems.append(f"{name} line {line}: {href} points at a missing anchor")

    for attrs, line in p.images:
        if "alt" not in attrs:
            problems.append(f"{name} line {line}: image without alt text")
        if not (attrs.get("width") and attrs.get("height")) and "lightbox__image" not in attrs.get("class", ""):
            problems.append(f"{name} line {line}: image without width and height")
        t = local_target(page, attrs["src"]) if attrs.get("src") else None
        if t and not t[0].exists():
            problems.append(f"{name} line {line}: image {attrs.get('src')} is missing")

    levels = [h for h, _ in p.headings]
    if levels and levels.count(1) > 1:
        problems.append(f"{name}: more than one h1")
    for (prev, _), (cur, line) in zip(p.headings, p.headings[1:]):
        if cur > prev + 1:
            problems.append(f"{name} line {line}: heading jumps from h{prev} to h{cur}")

    for block in p.jsonld:
        try:
            json.loads(block)
        except json.JSONDecodeError as e:
            problems.append(f"{name}: JSON-LD does not parse ({e})")


def check_agent_files(problems: list):
    for f in ("llms.txt", "robots.txt"):
        if not (ROOT / f).exists():
            problems.append(f"{f}: missing")
    llms = (ROOT / "llms.txt").read_text(encoding="utf-8") if (ROOT / "llms.txt").exists() else ""
    for url in re.findall(r"https://thesetox\.github\.io/[^\s)]*", llms):
        path = urlparse(url).path.lstrip("/")
        if path.startswith(OTHER_REPOS):
            continue
        target = ROOT / (path or "index.html")
        if not target.exists():
            problems.append(f"llms.txt: {url} points at a missing file")


def main() -> int:
    problems, anchors = [], {}
    for name in PAGES:
        check_page(name, problems, anchors)
    check_agent_files(problems)
    if problems:
        print("FAIL")
        print("\n".join(f"- {p}" for p in problems))
        return 1
    print(f"OK: {len(PAGES)} pages, links, images, headings, JSON-LD and agent files")
    return 0


if __name__ == "__main__":
    sys.exit(main())
