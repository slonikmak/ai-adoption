# Engineering the AI-Ready Organization

**Anton Mashkov · White paper v0.3**

A standalone white paper on human-centered AI adoption across the software development lifecycle. Anton Mashkov presents his view of the AI adoption engineer’s role through an illustrative calendar feature and a bounded pilot.

[English edition](https://slonikmak.github.io/ai-adoption/) · [Русская версия](https://slonikmak.github.io/ai-adoption/ru/)

The Russian edition lives in `ru/` and shares the site assets. Each edition includes its own HTML, Markdown and downloadable PDF.

## Open locally

No build, package manager, API keys, or network access required. Open `index.html` directly in a browser, or run a local HTTP server from this directory:

```bash
python3 -m http.server 8000
```

Then open <http://localhost:8000>. Press Ctrl+C in the terminal to stop the server.

## Project structure

```text
ai-ready-organization/
├── index.html             # Canonical document content and semantic page markup
├── assets/
│   ├── styles.css         # Layout, typography, responsive and print styles
│   ├── main.js            # Chapter highlighting, progress, mobile navigation, print
│   └── favicon.svg
├── content.md             # Generated, editable reading copy of the white paper
├── tools/
│   └── export_markdown.py # Optional Markdown export (Python standard library)
├── README.md
├── .nojekyll              # Publish static files unchanged on GitHub Pages
└── .gitignore
```

## Edit the document

- Text, section order, figures, and implementation backlog: `index.html`.
- Colors, fonts, spacing, layout, mobile breakpoints: `assets/styles.css`.
- Navigation and print behavior: `assets/main.js`.

`index.html` is the source of truth. `content.md` is a portable text snapshot, not an input to the web page. After editing the HTML, regenerate the Markdown snapshot:

```bash
python3 tools/export_markdown.py
```

All resources are local. The document uses system fonts and a fixed light color scheme, avoiding dependence on external themes. Chapters use ordinary anchor links; they can be bookmarked and linked directly, and navigation remains available if JavaScript is disabled on desktop.

## Print or save as PDF

Use **Download PDF** for the ready-to-share [PDF edition](output/pdf/ai-ready-organization.pdf). When the page is open in its own browser tab, **Print** opens the native print dialog with the full backlog expanded. To refresh the downloadable edition after a content change, print the current page to PDF with backgrounds on and browser headers and footers off, then replace the linked file.

## GitHub Pages

The [published paper](https://slonikmak.github.io/ai-adoption/) is served from the root of the `main` branch. Push updates to that branch to publish a new revision.

## Scope of this version

Version 0.3 follows a meeting-rescheduling feature from design review through verification and shows how a team decides whether to expand the pilot. The eight chapters and implementation backlog provide supporting detail.
