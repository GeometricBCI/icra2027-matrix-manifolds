# ICRA 2027 workshop placeholder website

Title: Matrix Manifold Methods in Engineering

Subtitle: Robotics and Brain-Computer Interfaces

This static page contains the proposed workshop title, a short description, the seven organizers, a contact address, and the construction and acceptance status.

## Files

- `docs/index.html`: website content
- `docs/styles.css`: responsive styling
- `docs/assets/robot-arm-illustrated.webp`: active cartoon robot illustration
- `docs/assets/matrix-surface-storybook.svg`: pastel cartoon treatment of the analytic SPD(2) surface
- `docs/assets/field-notes.svg`, `geometry-friends.svg`, and `letter.svg`: small original vector illustrations used across the page
- `docs/assets/`: illustration assets, favicon, and self-hosted fonts with licenses
- `tools/generate-matrix-surface.py`: reproducible source for the geometric illustration
- `artwork/`: original robot illustration and its generation prompt/provenance

No build step, JavaScript, third-party requests, or runtime dependencies are required. Open `docs/index.html` locally or serve the `docs` directory with a static web server. Keep the full `docs` directory together.

The design uses Source Serif 4, Klee One, and IBM Plex Sans, warm ivory, muted sage, charcoal, and small terracotta accents. Klee One adds a handwritten feel to the supporting text. Font files are served by the website, with their original SIL Open Font License files in `docs/assets/fonts`. The hero combines a hand-drawn-style cartoon robot arm with an orthographic projection of the determinant-one surface in SPD(2); the highlighted curve is an affine-invariant geodesic. The pastel fill and small face are decorative; the grid and highlighted geodesic are generated from the same analytic parameterization. The artwork is illustrative and does not represent a particular team's equipment or a specific kinematic mapping. The source robot illustration and complete generation prompts are retained in `artwork/`. The earlier studio-rendering artwork is retained for reference.

Regenerate the active matrix surface with `python3 tools/generate-matrix-surface.py --storybook`. The `--illustrated` option produces the earlier sparse line drawing; running the script without either option regenerates the original engraving.

Navigation uses native page anchors. A skip link, visible keyboard focus, reduced-motion support, and responsive layouts are included. The site makes no third-party font or script requests.

The robot composition is reduced by approximately 20% on larger screens, with a separate compact tablet layout. Small notebook, geometric-companion, and envelope illustrations extend the warm storybook direction to the section headings and footer. These decorative SVGs are original code-native assets and are hidden from screen readers. No new factual claims or program commitments are introduced by the visual refinements.

Font sources:

- [Adobe Source Serif](https://github.com/adobe-fonts/source-serif)
- [IBM Plex](https://github.com/IBM/plex)
- [Fontworks Klee](https://github.com/fontworks-fonts/Klee); the official Google Fonts Latin WOFF2 subsets are self-hosted, with the Klee license included.

## Publication

Deploy the contents of `docs` as a static website. The page states that the workshop is proposed and subject to acceptance. Replace those statements only after acceptance is confirmed.

For GitHub Pages, publish the `main` branch and the `/docs` directory.

Public website: https://geometricbci.github.io/icra2027-matrix-manifolds/
