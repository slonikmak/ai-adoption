# Engineering the AI-Ready Organization

**Anton Mashkov · White paper v0.2**

A standalone English-language white paper on human-centered AI adoption across the software development lifecycle. This is the approved preview adapted into a static, editable website. The framework is a proposal informed by engineering practice, not a claim of completed company-wide implementation.

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

Use the **Print / PDF** control at the top of the page and select **Save as PDF** in the browser's print dialog. The print stylesheet removes navigation and expands the implementation backlog. A separate prebuilt PDF is not included.

## Publish on GitHub Pages

1. Create a new repository (for example, `ai-adoption-framework`).
2. Copy the **contents** of this directory to the repository root; commit and push them to `main`.
3. In the repository, open **Settings → Pages**.
4. Under **Build and deployment**, select **Deploy from a branch**, then branch `main` and folder `/ (root)`. Save.
5. Use the published URL shown by GitHub Pages. Relative asset paths support repository-level Pages URLs and subdirectories.

No GitHub Actions workflow or external hosting service is required for this deployment method. Review the document before making the repository or site public. No existing repositories were changed.

## Scope of this version

The eight chapters, diagrams, examples, and implementation backlog preserve the reviewed English preview. The page is standalone rather than embedded in ChatGPT; small layout adjustments make it use the available browser width. The previous agentic-development presentation and a Russian translation are not bundled in this version.
