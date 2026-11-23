---
name: Stephen Siapno
description: Stephen Siapno's career and products as one release history, the newest release on top.
colors:
  paper: "#f3f4f0"
  surface: "#ffffff"
  ink: "#121826"
  ink-2: "#343b4a"
  muted: "#586173"
  rule: "#d9dcd3"
  rule-strong: "#b6bab0"
  action: "#2d5bd7"
  action-hover: "#2349b4"
  action-ink: "#ffffff"
  added: "#12733f"
  added-bg: "#dcefe3"
  changed: "#2a55c9"
  changed-bg: "#e2e8fa"
  progress: "#855600"
  progress-bg: "#f8e8c4"
  tag-bg: "#121826"
  tag-ink: "#f3f4f0"
  sk-field: "#f4f5f8"
  sk-line: "rgba(14, 16, 24, 0.1)"
  sk-ink: "#0e1018"
  sk-muted: "#5c6172"
  mj-field: "#e3edd5"
  mj-ink: "#23401f"
  mj-shadow: "rgba(35, 64, 31, 0.45)"
  band: "#121826"
  band-ink: "#f3f4f0"
  band-muted: "#c3c8d2"
  band-action: "#2d5bd7"
  band-action-ink: "#ffffff"
  paper-dark: "#0e131c"
  surface-dark: "#151b26"
  ink-dark: "#eef1f5"
  ink-2-dark: "#c8ceda"
  muted-dark: "#9aa3b4"
  rule-dark: "#263041"
  rule-strong-dark: "#3b4659"
  action-dark: "#8fb0ff"
  action-hover-dark: "#b5caff"
  action-ink-dark: "#0b1222"
  added-dark: "#7ad7a1"
  added-bg-dark: "#13301f"
  changed-dark: "#a6bdff"
  changed-bg-dark: "#1a2546"
  progress-dark: "#f1c35f"
  progress-bg-dark: "#35290d"
  tag-bg-dark: "#eef1f5"
  tag-ink-dark: "#0e131c"
  sk-field-dark: "#06080d"
  sk-line-dark: "rgba(236, 238, 245, 0.16)"
  sk-ink-dark: "#eceef4"
  sk-muted-dark: "#a9aebd"
  mj-field-dark: "#1c2a19"
  mj-ink-dark: "#d9e8cc"
  mj-shadow-dark: "rgba(0, 0, 0, 0.55)"
  band-dark: "#070a10"
  band-ink-dark: "#eef1f5"
  band-muted-dark: "#a7afbf"
  band-action-dark: "#8fb0ff"
  band-action-ink-dark: "#0b1222"
typography:
  display:
    fontFamily: '"Inter Tight", "Inter", ui-sans-serif, system-ui, -apple-system, "Segoe UI", sans-serif'
    fontSize: "clamp(3.25rem, 1.4rem + 7vw, 6rem)"
    fontWeight: 600
    lineHeight: 0.96
    letterSpacing: "-0.04em"
  headline:
    fontFamily: '"Inter Tight", "Inter", ui-sans-serif, system-ui, -apple-system, "Segoe UI", sans-serif'
    fontSize: "clamp(2.2rem, 1.5rem + 2.6vw, 3.6rem)"
    fontWeight: 600
    lineHeight: 1
    letterSpacing: "-0.04em"
  year:
    fontFamily: '"Inter Tight", "Inter", ui-sans-serif, system-ui, -apple-system, "Segoe UI", sans-serif'
    fontSize: "26px"
    fontWeight: 600
    lineHeight: 1.1
    letterSpacing: "-0.035em"
  title:
    fontFamily: '"Inter Tight", "Inter", ui-sans-serif, system-ui, -apple-system, "Segoe UI", sans-serif'
    fontSize: "clamp(1.5rem, 1.2rem + 1.1vw, 2rem)"
    fontWeight: 600
    lineHeight: 1.12
    letterSpacing: "-0.03em"
  title-featured:
    fontFamily: '"Inter Tight", "Inter", ui-sans-serif, system-ui, -apple-system, "Segoe UI", sans-serif'
    fontSize: "clamp(1.8rem, 1.3rem + 2vw, 2.6rem)"
    fontWeight: 600
    lineHeight: 1.12
    letterSpacing: "-0.03em"
  subhead:
    fontFamily: '"Inter Tight", "Inter", ui-sans-serif, system-ui, -apple-system, "Segoe UI", sans-serif'
    fontSize: "20px"
    fontWeight: 600
    letterSpacing: "-0.02em"
  lead:
    fontFamily: '"Inter Tight", "Inter", ui-sans-serif, system-ui, -apple-system, "Segoe UI", sans-serif'
    fontSize: "clamp(1.25rem, 1.05rem + 0.75vw, 1.6rem)"
    fontWeight: 400
    lineHeight: 1.4
  body:
    fontFamily: '"Inter Tight", "Inter", ui-sans-serif, system-ui, -apple-system, "Segoe UI", sans-serif'
    fontSize: "17px"
    fontWeight: 400
    lineHeight: 1.6
  link:
    fontFamily: '"Inter Tight", "Inter", ui-sans-serif, system-ui, -apple-system, "Segoe UI", sans-serif'
    fontSize: "15.5px"
    fontWeight: 600
  button:
    fontFamily: '"Inter Tight", "Inter", ui-sans-serif, system-ui, -apple-system, "Segoe UI", sans-serif'
    fontSize: "15.5px"
    fontWeight: 650
    lineHeight: 1
  label:
    fontFamily: '"Inter Tight", "Inter", ui-sans-serif, system-ui, -apple-system, "Segoe UI", sans-serif'
    fontSize: "12.5px"
    fontWeight: 700
    lineHeight: 1
  brand:
    fontFamily: '"Manrope", "Inter Tight", ui-sans-serif, system-ui, sans-serif'
    fontSize: "20px"
    fontWeight: 800
    lineHeight: 1
    letterSpacing: "-0.035em"
  tag:
    fontFamily: '"JetBrains Mono", ui-monospace, "SF Mono", Menlo, monospace'
    fontSize: "14px"
    fontWeight: 600
    lineHeight: 1.3
  data:
    fontFamily: '"JetBrains Mono", ui-monospace, "SF Mono", Menlo, monospace'
    fontSize: "13.5px"
    fontWeight: 400
rounded:
  tag: "6px"
  row: "10px"
  radius: "14px"
  pill: "999px"
spacing:
  gutter: "16px"
  gutter-wide: "40px"
  rail: "120px"
  rail-gap: "32px"
components:
  header:
    backgroundColor: "{colors.paper}"
    textColor: "{colors.ink}"
    height: "64px"
  nav-link:
    textColor: "{colors.ink-2}"
    padding: "10px 0"
  button-primary:
    backgroundColor: "{colors.action}"
    textColor: "{colors.action-ink}"
    typography: "{typography.button}"
    rounded: "{rounded.pill}"
    padding: "0 20px"
    height: "48px"
  button-primary-hover:
    backgroundColor: "{colors.action-hover}"
  button-primary-sm:
    backgroundColor: "{colors.action}"
    textColor: "{colors.action-ink}"
    rounded: "{rounded.pill}"
    padding: "0 16px"
    height: "44px"
  button-primary-band:
    backgroundColor: "{colors.band-action}"
    textColor: "{colors.band-action-ink}"
    typography: "{typography.button}"
    rounded: "{rounded.pill}"
    padding: "0 20px"
    height: "48px"
  button-ghost-band:
    textColor: "{colors.band-ink}"
    typography: "{typography.button}"
    rounded: "{rounded.pill}"
    padding: "0 20px"
    height: "48px"
  link-out:
    textColor: "{colors.action}"
    typography: "{typography.link}"
    padding: "0 4px"
    height: "44px"
  link-out-strong:
    textColor: "{colors.action}"
    typography: "{typography.link}"
    rounded: "{rounded.pill}"
    padding: "0 12px 0 15px"
    height: "40px"
  link-in:
    textColor: "{colors.ink-2}"
    padding: "0 4px"
    height: "44px"
  tag:
    backgroundColor: "{colors.tag-bg}"
    textColor: "{colors.tag-ink}"
    typography: "{typography.tag}"
    rounded: "{rounded.tag}"
    padding: "4px 10px"
  tag-entry:
    backgroundColor: "transparent"
    textColor: "{colors.ink}"
    rounded: "{rounded.tag}"
    padding: "2px 8px"
  label-added:
    backgroundColor: "{colors.added-bg}"
    textColor: "{colors.added}"
    typography: "{typography.label}"
    rounded: "{rounded.tag}"
    padding: "5px 8px"
  label-changed:
    backgroundColor: "{colors.changed-bg}"
    textColor: "{colors.changed}"
    typography: "{typography.label}"
    rounded: "{rounded.tag}"
    padding: "5px 8px"
  label-progress:
    backgroundColor: "{colors.progress-bg}"
    textColor: "{colors.progress}"
    typography: "{typography.label}"
    rounded: "{rounded.tag}"
    padding: "5px 8px"
  badge-latest:
    backgroundColor: "{colors.added-bg}"
    textColor: "{colors.added}"
    rounded: "{rounded.pill}"
    padding: "4px 11px"
  chip:
    textColor: "{colors.ink-2}"
    rounded: "{rounded.pill}"
    padding: "3px 10px"
  status-live:
    backgroundColor: "{colors.added-bg}"
    textColor: "{colors.added}"
    rounded: "{rounded.pill}"
    padding: "3px 10px"
  status-progress:
    backgroundColor: "{colors.progress-bg}"
    textColor: "{colors.progress}"
    rounded: "{rounded.pill}"
    padding: "3px 10px"
  rail-node:
    backgroundColor: "{colors.paper}"
    size: "13px"
  rail-node-live:
    backgroundColor: "{colors.added}"
    size: "13px"
  rail-node-featured:
    size: "15px"
  shortstat:
    textColor: "{colors.muted}"
    typography: "{typography.data}"
  assets-panel:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.ink}"
    rounded: "{rounded.radius}"
    padding: "8px"
  asset-row:
    rounded: "{rounded.row}"
    padding: "10px 12px"
  asset-icon:
    rounded: "{rounded.row}"
    size: "40px"
  asset-icon-primary:
    backgroundColor: "{colors.action}"
    textColor: "{colors.action-ink}"
    rounded: "{rounded.row}"
    size: "40px"
  cover-siapknow:
    backgroundColor: "{colors.sk-field}"
    textColor: "{colors.sk-ink}"
    rounded: "{rounded.radius}"
    padding: "12px 12px 14px"
  cover-mj:
    backgroundColor: "{colors.mj-field}"
    textColor: "{colors.mj-ink}"
    rounded: "{rounded.radius}"
    padding: "26px 18px 18px"
  contact-band:
    backgroundColor: "{colors.band}"
    textColor: "{colors.band-ink}"
    padding: "72px 0 80px"
---

# Design System: Stephen Siapno

## Overview

**Creative North Star: "The Release Notes"**

The site is one version history. Stephen's career and products read as releases of a single product, newest on top: the latest release (who he is now, with an Assets panel beside it), then a dated rail of earlier releases back to 2016, a ruled Skills list and an inverted contact band. Its vocabulary is changelog grammar on a cool paper ground: calendar version tags, coloured change labels, dated entries with live nodes, shortstat counts and an assets list. It refuses the hero-plus-project-cards portfolio.

The page is text-first and ruled, at the density of a good release page: 1px rules, measured line lengths, and colour that carries meaning rather than decoration. Cobalt is the only action colour; green, blue and amber are change meaning. Pictorial colour appears in exactly two places, the covers of the two featured releases, each in its own product's identity: SiapKnow's own site, as a screenshot on SiapKnow's field, and Myrna & Judith's leaf field with fanned App Store screenshots.

It is static. Its one script, allowed in the CSP by its SHA-256 hash, only makes the section and in-page links work with the history filter; everything else is CSS. Light and dark both follow `prefers-color-scheme`, with no toggle, and motion is two CSS moments, both off under reduced motion: the Latest badge stamps in once, and rail nodes light as their release scrolls in. The 404 and redirect pages reuse `site.css`; the Writerside archive pages keep their own look and sit outside this system.

**Key Characteristics:**
- One release history, newest first; work enters as an entry on the rail, never as a card grid.
- Changelog devices are the whole vocabulary: calendar tags, a dated rail with live nodes, change labels, shortstat lines, an assets panel.
- Cool paper, navy ink and one cobalt action colour; status hues only where they mean something.
- Flat and ruled: 1px rules, tonal tints and an inverted band instead of elevation.
- Product colour lives only inside the two featured covers.
- Both colour schemes follow the system. The only JavaScript is the filter helper: Work in the menu selects Products, Experience selects Roles, and a link to a release the filter hides resets it to All.

## Colors

A cool, near-neutral paper-and-ink palette with one cobalt action colour; green, blue and amber are reserved for change meaning, and each product's colours stay inside its cover. Every token is a custom property on `:root`, redefined under `@media (prefers-color-scheme: dark)`; the `-dark` keys in the frontmatter are those dark values. An `-ink` token is the text colour that sits on its fill.

### Primary
- **Cobalt Action** (#2d5bd7; dark #8fb0ff): the primary button, outward links, links inside change lines and on the 404 and redirect pages, the resume row's icon tile, the skip link and the focus ring. **Deep Cobalt** (#2349b4; dark #b5caff) is its hover, and **Action Ink** (#ffffff; dark #0b1222) sits on it.

### Neutral
- **Cool Paper** (#f3f4f0; dark #0e131c): the page, the sticky header, the hollow rail node, and the browser theme colour.
- **Panel White** (#ffffff; dark #151b26): the Assets panel only.
- **Navy Ink** (#121826; dark #eef1f5): headings, body text, shortstat counts.
- **Slate Ink** (#343b4a; dark #c8ceda): leads, entry date ranges, roles, nav links, chips, skill definitions, footer links.
- **Pewter** (#586173; dark #9aa3b4): the hero meta line, file names and sizes, shortstat text, the history intro, the footer.
- **Rule** (#d9dcd3; dark #263041): section, entry and skills dividers, the header's bottom edge, the Assets panel border.
- **Strong Rule** (#b6bab0; dark #3b4659): the rail line and hollow node rings, chip outlines, entry-tag rings, the mail button ring, inward-link underlines.
- **Tag Fill / Tag Ink** (#121826 / #f3f4f0; dark #eef1f5 / #0e131c): the release tag, ink and paper swapped.

### Change labels
- **Shipped Green** (#12733f on its wash #dcefe3; dark #7ad7a1 on #13301f): New, Added and Shipped labels, the Latest badge, live status chips, filled rail nodes.
- **Changed Blue** (#2a55c9 on #e2e8fa; dark #a6bdff on #1a2546): Changed, Updated, Improved, Built, Led, Maintained and Current labels.
- **Progress Amber** (#855600 on #f8e8c4; dark #f1c35f on #35290d): In progress labels and in-progress status chips.

### Cover fields
- **SiapKnow Field** (#f4f5f8; dark #06080d): the SiapKnow cover, in SiapKnow's own paper (the light field and ink are the two colours of its mark), holding a screenshot of siapknow.com that swaps with the scheme. SiapKnow Hairline (rgba(14, 16, 24, 0.1); dark rgba(236, 238, 245, 0.16)) rings the cover, SiapKnow Muted (#5c6172; dark #a9aebd) sets the caption, and SiapKnow Ink (#0e1018; dark #eceef4) is the cover's text colour.
- **Leaf Field** (#e3edd5; dark #1c2a19): the Myrna & Judith cover, with Leaf Ink (#23401f; dark #d9e8cc) for the caption and Leaf Shadow (rgba(35, 64, 31, 0.45); dark rgba(0, 0, 0, 0.55)) under the screenshots.

### Contact band
- **Inverted Band** (#121826; dark #070a10): the contact close, with Band Ink (#f3f4f0; dark #eef1f5) text, Band Muted (#c3c8d2; dark #a7afbf) for the location line, and Band Cobalt (#2d5bd7 with #ffffff; dark #8fb0ff with #0b1222) for its primary button, which deepens on hover to Band Cobalt Hover (#2349b4; dark #b5caff).

### Named Rules
**The Meaning Rule.** Green, changed-blue and amber appear only as change meaning: green for what was added, shipped or is live; blue for what changed, was led or is current; amber only for what is in progress. A rail node turns green only when its entry carries a live status.

**The Cover Rule.** The `sk-*` and `mj-*` tokens never leave their covers. Outside them, a product appears only through its own icon or mark (44px entry icons, 22px inline marks).

**The Tint Rule.** Hover fills, tile fills and outlines are `color-mix(in srgb, <token> N%, transparent)` tints of an existing token, never new colours: ink at 5% (row hover) and 7% (icon tile); action at 9% (the resume row, outlined-link hover), 15% (resume row hover) and 45% (outlined-link border); added and progress at 35% (status borders); added at 40% (the Latest ring). On the band, the ghost border mixes band-ink 40% into band.

## Typography

**Display Font:** Inter Tight (with Inter, ui-sans-serif, system-ui)
**Body Font:** Inter Tight
**Brand Font:** Manrope, for the name in the header only
**Label/Mono Font:** JetBrains Mono (with ui-monospace, SF Mono, Menlo)

**Character:** The pairing matches siapknow.com, by the owner's choice. Inter Tight carries everything from the 6rem name to 12.5px labels, at 600 for headings with tracking that tightens as size grows; Manrope 800 is the wordmark; JetBrains Mono is the release metadata.

Fonts load from Google Fonts (`css2`, `display=swap`): Inter Tight 400 to 800 (variable), JetBrains Mono 400 and 600, Manrope 700 and 800. The 404 page loads the same link; the redirect pages load only `site.css`, so their single line renders in the fallback stack.

### Hierarchy
- **Display** (600, clamp(3.25rem, 1.4rem + 7vw, 6rem), 0.96, -0.04em, balanced wrap): the name as the home page's h1. The 404 page's h1 uses clamp(2.6rem, 1.6rem + 4vw, 4.5rem).
- **Headline** (600, clamp(2.2rem, 1.5rem + 2.6vw, 3.6rem), 1, -0.04em): Version history, Skills, Contact.
- **Year** (600, 26px, 1.1, -0.035em, tabular figures): rail year labels; 40px, right-aligned and sticky from 960px.
- **Title** (600, clamp(1.5rem, 1.2rem + 1.1vw, 2rem), 1.12, -0.03em): entry titles; the two featured entries use clamp(1.8rem, 1.3rem + 2vw, 2.6rem). A role after the name drops to 0.66em, 500, Slate Ink.
- **Subhead** (600, 20px, -0.02em): "What's new". The Assets title is 16px, 600, -0.01em.
- **Lead** (400, clamp(1.25rem, 1.05rem + 0.75vw, 1.6rem), 1.4, 30ch): the hero lead, in Slate Ink. The contact lead is clamp(1.25rem, 1rem + 1vw, 1.75rem), 1.35, 24ch.
- **Body** (400, 17px, 1.6): base text. Entry leads 17.5px (62ch); hero change lines 17.5px at 1.5 (60ch); entry change lines 16.5px (68ch).
- **Label** (700, 12.5px, line-height 1): change labels. The Latest badge is 13.5px 700; kind and status chips 13.5px 600; skill group names 720.
- **Button and Link** (15.5px): button labels at 650 (15px on the small button), outward links at 600, inward links at 500.
- **Brand** (Manrope 800, 20px, 1, -0.035em): the header name; 18px at 380px and under.
- **Tag** (JetBrains Mono 600, 14px, 1.3): the release tag; entry tags 12.5px.
- **Data** (JetBrains Mono 400, 13.5px): entry date ranges and shortstat lines, counts in 600 Navy Ink; file names 13px, sizes 12.5px.

### Named Rules
**The Six-Hundred Rule.** Every Inter Tight heading, from the 6rem name to the 16px panel title, is 600. Heavier weights belong to small text that has to hold at size: 650 for buttons and asset names, 700 for labels, badges and bold text, 720 for skill group names. Only the Manrope name reaches 800.

**The Tight-at-Size Rule.** Tracking tightens as size grows: -0.04em on display and headlines, -0.035em on years and the name, -0.03em on entry titles, -0.02em on the subhead and the contact email, -0.01em on the Assets title and entry roles. Body text keeps normal tracking.

**The Metadata Mono Rule.** JetBrains Mono sets only release metadata: calendar tags, entry date ranges, file names and handles in the Assets list, sizes, and shortstat counts. It never sets prose, headings, labels or buttons. Year labels and the hero's "Updated" date stay in Inter Tight.

## Layout

A single column of full-width sections inside a centred wrap (max 1240px), with side gutters of 16px (or the safe-area inset, if larger) at phone width and 40px from 720px.

- **The rail.** From 960px each year is a grid: a 120px year column (`--rail`), a 32px gap, then the entries; year labels sit right-aligned and sticky at 88px. Below 960px the year sits above its entries. Entries hang off a 1px Strong Rule line (6px in, 24px padding; flush, with 36px padding, from 960px), each node centred on the line.
- **First viewport.** From 960px the release notes and a 384px Assets panel sit side by side with a 64px gap; below, they stack 40px apart.
- **Featured entries.** From 1120px the notes and the cover (up to 380px) sit side by side 40px apart, the cover sticky at 96px; below, they stack 26px apart.
- **Change lines.** A 5.9rem label column with a 12px gap (6.4rem and 14px from 720px); at 559px and below the label runs inline before its text.
- **Skills.** Ruled rows; from 560px a 9.5rem term column with a 16px gap.
- **Contact.** From 960px two equal columns aligned to the bottom, 64px apart; stacked 32px apart below.
- **Vertical rhythm.** Section padding, top and bottom: latest 40 and 56px (76 and 92px from 960px); history 64 and 40px (88px top from 960px); skills 72px; contact 72 and 80px (96 and 104px from 960px); footer 28 and 40px; 404 and redirect pages 96px. Entries pad 24px above and 30px below (36px when featured) and are ruled between, except after the last in a year. Years sit 20px apart.
- **Header.** Sticky, a 64px row; anchors land below it through `scroll-padding-top: 84px`.

### Named Rules
**The Rail Alignment Rule.** From 960px the history and skills content starts at the rail offset, `calc(var(--rail) + 32px)`: the Version history head, the Skills heading and the skills list all line up with the entries column, not the page edge.

## Elevation & Depth

Flat. Page surfaces cast no shadows; depth is tonal: the white Assets panel on paper inside a 1px rule, tinted fills on hover and on the resume row, the inverted contact band, and the two cover fields. The sticky header is opaque paper over a 1px rule, with no shadow or blur.

### Shadow Vocabulary
- **Screenshot lift** (`box-shadow: 0 18px 30px -16px var(--mj-shadow), 0 2px 6px rgba(35, 64, 31, 0.12)`): only the three App Store screenshots in the Myrna & Judith cover.
- **Hairline ring** (`box-shadow: inset 0 0 0 1px <colour>`): a border that adds no size, on entry tags (Strong Rule), the Latest badge (Shipped Green at 40%) and the SiapKnow cover (SiapKnow Hairline).

### Named Rules
**The Flat Release Rule.** Surfaces rest flat; separation comes from 1px rules, tonal tints and inverted fields. The only cast shadow belongs to the product screenshots inside the Myrna & Judith cover.

## Shapes

- **Pills** (999px): buttons, outlined links, the Latest badge, kind and status chips.
- **Tag corners** (6px): calendar tags, change labels, the 22px inline marks.
- **Row corners** (10px): asset rows, their 40px icon tiles, the skip link.
- **Panel corners** (14px, `--radius`): the Assets panel and both covers.
- **Circles:** rail nodes (13px; 15px when featured), the 44px header mail button.
- **Own shapes:** 44px entry icons keep app-icon corners (11px); the Myrna & Judith screenshots take 16px, the siapknow.com screenshot 9px.
- **Lines:** 1px rules and borders throughout; 2px node rings; the contact email's 2px underline (3px on hover).
- **Favicon:** a label tag in Navy Ink with a Cool Paper eyelet, swapped in dark.

### Named Rules
**The Label-Versus-State Rule.** Change labels and calendar tags are 6px rectangles; kind and status chips are pills. "Shipped" (a change) and "Live on iOS and Android" (a state) share a colour, so shape tells them apart.

## Components

### Buttons
- **Shape:** full pill (999px), 48px tall, 20px side padding, a trailing 18px stroke icon 8px after the label.
- **Primary:** Cobalt Action fill, Action Ink label at 650. The header's small variant is 44px tall, 16px padding (14px below 760px), 15px label.
- **Ghost:** transparent with a 1px border (Strong Rule on paper; on the band, band-ink mixed 40% into band) and the text colour for its label. It appears only in the contact band today.
- **Hover / Active:** primary deepens to Deep Cobalt; a ghost border turns to the text colour; a press drops the button 1px. Background, border and transform transition over 0.2s on `--ease-out` (cubic-bezier(0.16, 1, 0.3, 1)).
- **Focus (everything):** a 2px Cobalt Action outline at 3px offset; elements without their own radius take 4px corners while focused. Inside the contact band the outline is band-ink.

### Links
- **Outward:** Cobalt Action, 600, 15.5px, a trailing 16px arrow, 44px tall; underline at 4px offset on hover.
- **Outlined:** the outward link inside a pill border of action at 45%, 40px tall, padded 0 12px 0 15px; on hover it fills with action at 9% instead of underlining. It marks an entry's lead destinations: the studio site, store listings, the diagram viewer, the article series.
- **Inward:** Slate Ink, 500, underlined in Strong Rule; the underline takes the text colour on hover. Used for "Full notes" into the archive.
- **In change lines:** Cobalt Action, 600, underline at 3px offset; a product name can lead with its 22px inline mark.
- **Links row:** wraps with 8px by 10px gaps, 18px below the content above.

### Calendar tags
- **Release tag:** Tag Fill with Tag Ink, JetBrains Mono 600 14px, 4px by 10px, 6px corners. It marks the latest release (2026.11) and the 404 page.
- **Entry tag:** transparent with a Strong Rule hairline ring, Navy Ink, 12.5px, 2px by 8px. It opens every entry's meta row.
- **Format:** calendar versions, YYYY.MM (2026.04), or the year alone (2023) when the month isn't recorded.

### Change lines
- **Anatomy:** a coloured verb label, then the note. Labels are 12.5px 700, 5px by 8px, 6px corners, a tinted wash with matching ink, nudged up 1px to sit on the text's baseline.
- **Mapping (as built):** Shipped Green for New, Added and Shipped; Changed Blue for Changed, Updated, Improved, Built, Led, Maintained and Current; Progress Amber for In progress.
- **Spacing:** hero lines run 17.5px with 14px between lines; entry lines 16.5px with 12px.

### Status chips and the Latest badge
- **Meta row order:** entry tag, then a mono date range when the release spans time ("Apr 2026 – now"; a single-date release shows only its tag), kind chip, then any status chips; 8px by 10px gaps, 13.5px.
- **Kind and neutral status:** pill, 1px Strong Rule border, Slate Ink, 600, 3px by 10px. Kinds: Studio, App, Open source, Tool, Role, Writing, Education. Neutral statuses carry dated facts ("29 stars · Nov 2026", "Private repository").
- **Live:** Shipped Green on its wash with a 35% green border ("Running", "Live on iOS and Android", "Current"). **In progress:** Progress Amber on its wash with a 35% amber border.
- **Latest badge:** Shipped Green pill, 4px by 11px, 13.5px 700, with a 40% green hairline ring. Only the latest release wears it, and it stamps in once on load (0.75s, from 1.7× scale, -7° and a 2px blur to rest).

### Dated rail
- **Line:** 1px Strong Rule down the left of each year's entries.
- **Nodes:** a 13px circle per entry (15px when featured), centred on the line beside the title: hollow (Cool Paper with a 2px Strong Rule ring) by default, solid Shipped Green when the entry has a live status.
- **Entry anatomy:** title (optional 44px app icon, optional role), meta row, lead (17.5px Slate Ink, bold in Navy Ink), change lines, shortstat, links row.
- **Motion:** as an entry scrolls in, its node grows from half size, and a live node fills from hollow to green (a scroll-driven `view()` timeline from entry 0% to cover 30%), only where supported.

### History filter
- **Chips:** All, Products, Roles, and Open source & writing, as radio inputs styled as 44px pills: a 1px Strong Rule border, 15px Slate Ink 600 text, 16px side padding, 8px apart. The selected chip fills with Navy Ink and Paper text. The focus ring goes on the chip's label.
- **Behaviour:** pure CSS with `:has()`. A chip hides entries of other kinds and any year left empty. Work and Experience in the menu select Products and Roles; a link to a hidden release resets the filter to All.

### Shortstat lines
- JetBrains Mono 13.5px in Pewter, counts in 600 Navy Ink, items wrapping with 4px by 18px gaps, 18px below the change lines. Each line ends with the date it was counted ("Counted Nov 18, 2026").

### Assets panel
- **Panel:** Panel White, 1px Rule border, 14px corners, 8px padding; the title sits at 12px 12px 8px.
- **Rows:** a 40px icon tile and the text, 14px apart, at least 62px tall, padded 10px by 12px, 10px corners, 2px between rows. Hover tints ink at 5%; the tile is ink at 7%.
- **Resume row (primary):** action at 9% (15% on hover), with a solid Cobalt Action tile and an Action Ink icon. It always leads; Email, LinkedIn, GitHub and llms.txt follow.
- **Text:** name 16px 650; file name or handle in mono 13px Pewter, truncated with an ellipsis; size and date on their own mono 12.5px line beneath at every width, so the name always shows in full.

### Featured covers
- **Frame:** 14px corners, clipped; a centred caption, 13.5px 600, under the picture. From 1120px the cover sits beside the notes, sticky at 96px.
- **SiapKnow:** SiapKnow Field inside a SiapKnow Hairline inset ring, padded 12px 12px 14px with 12px between its parts: a full-width screenshot of siapknow.com with 9px corners (a `<picture>` that serves the dark capture under `prefers-color-scheme: dark`), then the caption "siapknow.com" in SiapKnow Muted.
- **Myrna & Judith:** Leaf Field, padded 26px 18px 18px with 14px between its parts: three App Store screenshots fanned from the bottom centre (the outer two at ∓5°, 0.9 scale, pulled 14% inward; the middle one on top), each 34% wide up to 156px with 16px corners and the screenshot lift; then the caption in Leaf Ink.

### Navigation
- **Header:** sticky, opaque Cool Paper, 1px Rule bottom edge, a 64px row with 24px gaps: the Manrope name, the section links, the small primary Resume button. Below 760px the gap tightens to 8px and the Resume pill to 14px side padding; at 380px and under the name drops to 18px.
- **Section links** (Work, Experience, Skills, Contact): 15px Slate Ink, 28px apart, 10px vertical padding; hover turns Navy Ink with an underline at 6px offset. They show from 760px; below that, a 44px circular mail button (Strong Rule ring, Navy Ink ring on hover) takes their place.
- **Skip link:** parked above the viewport, it drops to 12px from the top on focus; Cobalt Action fill, 10px corners, 600.

### Contact band
- Inverted Band with Band Ink text, padded 72px and 80px (96px and 104px from 960px). The email is set large (clamp(1.2rem, 0.75rem + 1.5vw, 1.85rem), 600, -0.02em) with a 2px underline at 7px offset, 3px on hover, wrapping anywhere. Below it sit the primary button in Band Cobalt and ghost buttons for LinkedIn and GitHub, 10px apart. In dark mode a 1px Rule top edge separates the band from the page.

### Footer
- 14.5px Pewter; links in Slate Ink with 44px targets and underlines at 4px offset; wraps with 8px by 28px gaps.

### 404 and redirect pages
- The wrap with 96px above and below. A redirect page carries one 19px Slate Ink line with a Cobalt Action link (600) and refreshes into its home-page section. The 404 shows its status as a release tag, then the smaller display h1 and a lead.

## Do's and Don'ts

### Do:
- **Do** add new work as an entry in its year: entry tag, a mono date range if it spans time, kind chip, status, then change lines that each open with one coloured verb.
- **Do** pick label colours by meaning: Shipped Green for New, Added and Shipped; Changed Blue for Changed, Updated, Improved, Built, Led, Maintained and Current; Progress Amber only for In progress.
- **Do** date every count: shortstat lines end with "Counted <date>", and star counts carry their month.
- **Do** define every new colour twice, in `:root` and in the `prefers-color-scheme: dark` block.
- **Do** derive hovers, tile fills and outlines from existing tokens with `color-mix` (5 to 15% fills, 35 to 45% borders).
- **Do** keep keyframe animation and smooth scrolling behind `prefers-reduced-motion: no-preference`, on `--ease-out`, in CSS only.

### Don't:
- **Don't** present work as a hero with project cards or a card grid; it enters the history as a release.
- **Don't** set prose, headings, labels or buttons in JetBrains Mono.
- **Don't** use the `sk-*` or `mj-*` tokens outside their covers.
- **Don't** give page surfaces drop shadows; borders may be 1px inset rings, and the only cast shadow is the screenshot lift inside the Myrna & Judith cover.
- **Don't** set Inter Tight headings above 600, or use Manrope for anything but the header name.
- **Don't** make a status chip or rail node green for anything that isn't live now; green chips mean live, running or current.
- **Don't** add a theme toggle or more JavaScript; both schemes follow `prefers-color-scheme`, and the home page's CSP allows only the filter helper, by its SHA-256 hash. If that script changes, update the hash in the CSP.
