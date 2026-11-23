# Product

<!-- impeccable:product-schema 1 -->

## Platform

web

## Stack

**Chosen: B, hand-built static HTML/CSS** (the user's choice, 2026-11-23). Two proposals were compared first:

- **A: JetBrains Writerside.** Source in `TheSetox/StephenSiapno` (`Writerside/`, instance `ss`), built with the `jetbrains/writerside-builder` Docker image, output copied into this repo.
- **B: hand-built static HTML/CSS** written directly in this repo, like siapknow.com.

GitHub Pages serves this repo's `main` branch root (legacy Jekyll build). No custom domain: the site is https://thesetox.github.io/.

## Users

Primary: hiring teams, meaning recruiters and engineering managers hiring for mobile (Android, Kotlin Multiplatform) and AI-first engineering roles (the user's answer, 2026-11-23). They arrive from a resume, LinkedIn or GitHub, on a work desktop or a phone. They scan for the role, seniority, shipped work and a way to reach him.

Secondary: engineers and studio contacts who follow links from siapknow.com.

## Product Purpose

Stephen Siapno's personal site. Within seconds, a hiring team should understand that he is a mobile engineer (Android since 2016, Kotlin Multiplatform) who builds AI-first. They should then see the proof and get his resume or contact him.

Success means the visitor downloads the resume, emails him, or opens his LinkedIn.

## Positioning

He does more than use AI tools. He runs SiapKnow, an AI-first studio where AI agents, working under his direction and approval gates, build and ship real products. Myrna & Judith is live on the App Store and Google Play, and siapknow.com describes it as built with "no manual development". Alongside that, he has ten years of production Android and Kotlin Multiplatform engineering (EROAD, Digiplus, Accenture and earlier). Together these make the claim a neighbouring engineer can't copy.

The user: "I want to build my website as AI-first; that is why I created siapknow.com."

## Operating Context

- Hiring flow: resume screens, LinkedIn, the GitHub profile (`TheSetox`), interviews.
- AI-first also means the site must be readable by AI agents and recruiting tools: semantic HTML, structured data and a plain-text summary for agents.
- The user's studio site (siapknow.com, repo `siapknow-website`) is the proof the personal site points to.

## Capabilities and Constraints

- Static hosting only: no backend, forms, cookies or analytics.
- Existing public URLs keep working: `about-me.html`, `portfolio.html`, `experience.html`, `contact.html`, `myrna-and-judith.html`, the company and project pages, the technical notes, and the article pages linked from Medium.
- Contact: his personal Gmail, as on the current Contact page (the user's choice, 2026-11-23), plus LinkedIn (`linkedin.com/in/stephen-siapno`) and GitHub (`github.com/TheSetox`).
- Resume: `resources/stephen_siapno_cv.pdf`, exported Nov 23, 2026 from the owner's Google Doc ("stephen.siapno_cv_2026"). It now lists Android on Google Play and the corrected Mobext role.
- Projects: everything he has built that has value. SiapKnow and Myrna & Judith lead. Projects without value, such as ConversionApp, are left out, unless a project showcases architecture (the user's answer, 2026-11-23).

## Brand Commitments

- Name: Stephen Siapno. Handle: TheSetox.
- SiapKnow calls itself an "AI-first studio". Its site is https://siapknow.com.
- Myrna & Judith: Judith (bills), Myrna (paydays) and Insight (the month's numbers). Write "Insight", never "Mr. Insights". Tagline: "Know what's due before payday."
- Typography matches siapknow.com: Inter Tight for text and headings, Manrope for the name, JetBrains Mono for data (the user's choice for proposal B, 2026-11-23).

## Evidence on Hand

- **SiapKnow record**, counted Nov 18, 2026 from git, GitHub and session logs, since Apr 2026:
  - 5,341 commits across 8 repositories, 84% co-written in Claude Code
  - 334 of 367 pull requests merged
  - 907K lines of code, plus 128K lines of docs
  - 6,485 automated tests in Myrna & Judith
  - 2,057 agent hours in 47 days
  - 1,257 sub-agent runs across 79 sessions, with up to 26 at once
  - 34 Reels and films
  - 55 artifacts

  Also on siapknow.com: 5 releases and 41 harness updates; the video pipeline's 32 Reels and 2 films; 291 app pull requests merged and 31 store builds.
  These numbers are refreshed by hand only, when the user asks (`siapknow-website/tools/metrics.py`).
- **Myrna & Judith:**
  - Live on the App Store (`id6767477202`) and Google Play (`app.myrnaandjudith`): free, Android 8.0 or later.
  - Website: https://myrnaandjudith.com.
  - Built with Kotlin Multiplatform and Compose Multiplatform: offline-first, no account or backend, Firebase Analytics and Crashlytics.
  - The first production version was built in two weeks.
  - Counts: 3,930 commits on main, 291 PRs merged, 25 modules, 31 store builds, 292K Kotlin lines.
- **CommitPath:** a free, offline-first Kotlin knowledge refresher with flashcards and guided lessons. It's on the App Store (`id6816756095`), its site is https://thesetox.github.io/commitpath-site/, and version 2 (AI flashcards) is in progress.
- **MainHarness:** a portable delivery harness that turns AI agents (Codex, GitHub Copilot, Claude Code) into a disciplined team: 17 skills, 5 roles, 12 rule sets and 9 tools. The repo is private and is described publicly on siapknow.com.
- **Toolbox:** an AI tool for developers, in progress. It has no public page.
- **Architecture work:**
  - KMP Sample Diagrams (29 stars): https://thesetox.github.io/kmp-sample-diagrams/
  - KMP Fun Clean Architecture (13 stars), with docs at https://thesetox.github.io/KMP-Playground-Document/introduction.html
  - The "Fluent and Fun Clean Architecture" article series on ProAndroidDev (Medium), also featured on the droidcon website (per his own notes page)
  - Star counts (29 and 13) as of Nov 2026
- **Experience** (resume, September 2026):
  - EROAD, Mobile Engineer (June 2025 to present)
  - Digiplus, Android Developer (October 2024 to May 2025)
  - Accenture, Android Engineer (February 2020 to October 2024)
  - Yondu (2018 to 2019)
  - Auspex Corp (2017 to 2018)
  - Mobext (2016 to 2017): built the Bonifacio Global City iOS app from scratch in Xamarin (C#) with MVVM, in three months; maintained consumer apps. The September resume wrongly says he rebuilt an Android app (the user's correction, 2026-11-23).
  - BS Information Technology, University of Pangasinan (2016)
- **Assets:**
  - App Store screenshots: `siapknow-website/media/store-*.jpg` and `myrna-and-judith-store-kit/en-US/screenshots-6.9/`
  - Myrna & Judith app icon: `myrna-and-judith/iosApp/iosApp/Assets.xcassets/AppIcon.appiconset/app_icon_1024.png`
  - Character art and logos: `myrna-and-judith-website/img/`
  - Existing images in this repo: `images/myrna-*.webp`
- **Absences:** no testimonials, client list, availability, rates or salary. Never invent them.

## Product Principles

1. Proof over claims: every claim points at something live, such as a store listing, a site, a repo, or a counted number with its date.
2. Built for a hiring team's speed: the role, seniority, AI-first proof, resume and contact are all reachable from the first screen.
3. Readable by people and agents alike.
4. Old links never break.
5. Honest status: say what is live and what is in progress.

## Accessibility & Inclusion

WCAG 2.2 AA. Works at phone width, in light and dark, and with reduced motion. siapknow.com's checks (alt text, heading order, named links) are the bar.
