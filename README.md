# ICRA 2027 workshop placeholder website

Title: Matrix Manifold Methods in Engineering

Subtitle: Robotics and Brain-Computer Interfaces

This static page contains the proposed workshop title, a short description, the seven organizers, a contact address, and the construction and acceptance status.

## Files

- `docs/index.html`: website content
- `docs/styles.css`: responsive styling
- `docs/assets/`: robot artwork, geometric illustration, favicon, and self-hosted fonts with licenses
- `tools/generate-matrix-surface.py`: reproducible source for the geometric illustration
- `artwork/`: original robot illustration and its generation prompt/provenance

No build step, JavaScript, third-party requests, or runtime dependencies are required. Open `docs/index.html` locally or serve the `docs` directory with a static web server. Keep the full `docs` directory together.

The design uses Source Serif 4 and IBM Plex Sans, warm ivory, graphite, and a restrained rust accent. Font files are served by the website, with their original SIL Open Font License files in `docs/assets/fonts`. The hero combines a conceptual robot-arm rendering with an orthographic projection of the determinant-one surface in SPD(2); the highlighted curve is an affine-invariant geodesic. The artwork is illustrative and does not represent a particular team's equipment or a specific kinematic mapping. The original robot asset and exact generation prompt are retained in `artwork/`.

Navigation uses native page anchors. A skip link, visible keyboard focus, reduced-motion support, and responsive layouts are included. The site makes no third-party font or script requests.

Font sources:

- [Adobe Source Serif](https://github.com/adobe-fonts/source-serif)
- [IBM Plex](https://github.com/IBM/plex)

## Publication

Deploy the contents of `docs` as a static website. The page states that the workshop is proposed and subject to acceptance. Replace those statements only after acceptance is confirmed.

For GitHub Pages, publish the `main` branch and the `/docs` directory.

Public website: https://geometricbci.github.io/icra2027-matrix-manifolds/
