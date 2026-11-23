# thesetox.github.io

Stephen Siapno's personal site, served by GitHub Pages from this repo's `main` branch root (legacy Jekyll build, no custom domain). It is written for hiring teams first, and it is readable by AI agents too.

This branch holds **proposal B, the hand-built site**. Proposal A, the same content built with JetBrains Writerside, is on the `codex/writerside-redesign` branch; its source is `TheSetox/StephenSiapno`.

## Files

| Path | What it is |
|---|---|
| `index.html` | The home page, one version history: the latest release (who he is now), then products, roles and writing back to 2016. It also holds the page's JSON-LD (Person, SiapKnow, the apps). |
| `site.css` | All styles. Tokens at the top: colours for light and dark, and the fonts (Inter Tight, Manrope, JetBrains Mono, matching siapknow.com). |
| `media/` | Web copies of the app icons and three Myrna & Judith App Store screenshots. The masters live in the app and store-kit repos. |
| `llms.txt` | The plain-text summary for AI agents (llmstxt.org format). Keep it in step with `index.html`. |
| `robots.txt`, `sitemap.xml` | Crawlers are welcome; the sitemap lists the home page and the archive pages. |
| `404.html`, `favicon.svg` | The not-found page and the tab icon. |
| `about-me.html`, `portfolio.html`, `experience.html`, `contact.html`, `myrna-and-judith.html`, `siapknow.html` | Old or linked addresses. Each one sends visitors to its section of the home page. |
| Everything else (`notes.html`, the company and project pages, `static/`, `images/`, `resources/`, `HelpTOC.json`, `Map.jhm`, `config.json`) | The archive: Writerside pages kept at their original URLs. Rebuild them from `TheSetox/StephenSiapno`. |
| `PRODUCT.md`, `DESIGN.md` | Product truth and the design system. Jekyll leaves them off the public site (`_config.yml`). |
| `tools/check.py` | The checks below. Also kept off the public site. |

## Updating

- **The numbers** (commits, pull requests, tests, agent hours) mirror siapknow.com's record, counted on Nov 18, 2026. They are refreshed by hand only. When siapknow.com is recounted, update `index.html` and `llms.txt` to match, along with the dates beside them.
- **The resume** is `resources/stephen_siapno_cv.pdf`, exported from the owner's Google Doc (last exported Nov 23, 2026). When the doc changes, export it again and update the size and date on the Resume row in `index.html`.
- **A new release:** add an `article.entry` to the right year in `index.html`, then a line in `llms.txt`.

## Checks

```bash
python3 -I tools/check.py
```

This checks the new pages for unclosed tags, duplicate ids, missing files and anchors, `http://` links, images without alt text or size, skipped heading levels, JSON-LD that doesn't parse, and links in `llms.txt` that point nowhere.

## Preview

```bash
python3 -m http.server 8812
```

Then open http://localhost:8812/.

## Publishing

Pushing to `main` publishes the site. Every push is the owner's call.
