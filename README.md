# thesetox.github.io

Stephen Siapno's personal site, served by GitHub Pages from this repo's `main` branch root (legacy Jekyll build, no custom domain). It is written for hiring teams first, and it is readable by AI agents too.

The site is hand-built: what is in this repo is what GitHub Pages serves, with no build step. It replaced the JetBrains Writerside site (source: `TheSetox/StephenSiapno`), which nothing here depends on any more.

## Files

| Path | What it is |
|---|---|
| `index.html` | The home page, one version history: the latest release (who he is now), then products, roles and writing back to 2016. It also holds the page's JSON-LD (Person, SiapKnow, the apps). |
| `site.css` | All styles. Tokens at the top: colours for light and dark, and the fonts (Inter Tight, Manrope, JetBrains Mono, matching siapknow.com). |
| `media/` | Web copies of the app icons and three Myrna & Judith App Store screenshots. The masters live in the app and store-kit repos. |
| `llms.txt` | The plain-text summary for AI agents (llmstxt.org format). Keep it in step with `index.html`. |
| `robots.txt`, `sitemap.xml` | Crawlers are welcome; the sitemap lists the home page and the archive pages. |
| `404.html`, `favicon.svg` | The not-found page and the tab icon. |
| `notes.html` | The full notes: every role since 2016 with the projects inside it, and the Fluent and Fun Clean Architecture series. Same design as the home page. |
| Every other `.html` page except `404.html` | An old address (the Writerside site and its company, project, skills and personal pages). Each one redirects to its section of the home page or the notes page, so old links keep working. |
| `resources/stephen_siapno_cv.pdf` | The resume. |
| `PRODUCT.md`, `DESIGN.md` | Product truth and the design system. Jekyll leaves them off the public site (`_config.yml`). |
| `tools/check.py` | The checks below. Also kept off the public site. |

## Updating

- **The numbers** (commits, pull requests, tests, agent hours) mirror siapknow.com's record, recounted on Nov 23, 2026. They are refreshed by hand only. When siapknow.com is recounted, update `index.html` and `llms.txt` to match, along with the dates beside them.
- **The previews**: `media/siapknow-preview-{light,dark}.webp` are siapknow.com screenshots (headless Chrome, 1440×900 at 2x, reduced motion so the counters show final numbers), with `-large` copies for the zoom. Retake them when siapknow.com changes. The Myrna & Judith `-large` screenshots come from the store kit.
- **The resume** is `resources/stephen_siapno_cv.pdf`, exported from the owner's Google Doc (last exported Nov 23, 2026). When the doc changes, export it again and update the size and date on the Resume row in `index.html`.
- **A new release:** add an `article.entry` to the right year in `index.html`, then a line in `llms.txt`. For a role, add its long version to `notes.html` too.
- **The filter script:** `index.html` allows its one inline script by SHA-256 hash in the CSP. If you change the script, update the hash, or the browser will block it.

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
