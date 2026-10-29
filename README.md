# ICRA 2027 workshop placeholder website

Title: Matrix Manifold Methods in Engineering

Subtitle: Robotics and Brain-Computer Interfaces

This static page contains the proposed workshop title, a short description, the seven organizers, a contact address, and the construction and acceptance status.

## Files

- `docs/index.html`: website content
- `docs/styles.css`: responsive styling
- `docs/assets/shared-workbench-car-illustrated.webp`: active hand-painted scene of Shin-chan watching the robot grasp a toy car on their shared workbench
- `docs/assets/matrix-surface-storybook.svg`: pastel cartoon treatment of the analytic SPD(2) surface
- `docs/assets/field-notes.svg`, `team-birds.svg`, and `letter.svg`: small original vector illustrations used across the page
- `docs/assets/`: illustration assets, favicon, and self-hosted fonts with licenses
- `tools/generate-matrix-surface.py`: reproducible source for the geometric illustration
- `artwork/`: source illustrations and their generation prompts/provenance

No build step, JavaScript, third-party requests, or runtime dependencies are required. Open `docs/index.html` locally or serve the `docs` directory with a static web server. Keep the full `docs` directory together.

The design uses Source Serif 4, Klee One, and IBM Plex Sans, warm ivory, muted sage, charcoal, and small terracotta accents. Klee One adds a handwritten feel to the supporting text. Font files are served by the website, with their original SIL Open Font License files in `docs/assets/fonts`. The hero places an orthographic projection of the determinant-one surface in SPD(2) above a shared workbench scene; the highlighted curve is an affine-invariant geodesic. The pastel fill and subtle pigment texture are decorative; the grid and highlighted geodesic are generated from the same analytic parameterization. The surface is separate from the robot's grasped object. The artwork is illustrative and does not represent a particular team's equipment or a specific kinematic mapping. Source illustrations and complete generation prompts are retained in `artwork/`. Earlier standalone and studio-rendering assets are retained for reference.

Regenerate the active matrix surface with `python3 tools/generate-matrix-surface.py --storybook`. The `--illustrated` option produces the earlier sparse line drawing; running the script without either option regenerates the original engraving.

Navigation uses native page anchors. A skip link, visible keyboard focus, reduced-motion support, and responsive layouts are included. The site makes no third-party font or script requests.

The page has a centered maximum content width of 940px, slightly widened from 890px to give institution names more room. Organizer entries contain names and institutions, without country labels or research-area descriptions. Heading sizes, column gaps, and the hero composition are adjusted to suit the narrower page; small screens retain comfortable reading margins. Shin-chan wears an external EEG cap and leans forward as the robot grasps a small toy car resting on their shared workbench. His hands, a cap lead and small recording box, the tabletop, and the inward robot pose connect the scene. The analytic matrix surface is above both subjects. This visual metaphor introduces the BCI theme; it does not depict a demonstrated robot-control system or an electrode montage. The built-in imagegen prompt and source PNG are retained in `artwork/ART_DIRECTION_TOY_CAR_SCENE.md` and `artwork/shared-workbench-car-illustrated.png`. The surface retains a sparse grid and has no facial features; its SPD(2) and determinant labels use handwritten lettering on a paper-like tag directly below the surface. Notebook, bird-trio, and envelope illustrations extend the same direction to the section headings and footer. These decorative SVGs are original code-native assets and are hidden from screen readers. No new factual claims or program commitments are introduced by the visual refinements.

Font sources:

- [Adobe Source Serif](https://github.com/adobe-fonts/source-serif)
- [IBM Plex](https://github.com/IBM/plex)
- [Fontworks Klee](https://github.com/fontworks-fonts/Klee); the official Google Fonts Latin WOFF2 subsets are self-hosted, with the Klee license included.

## Publication

Deploy the contents of `docs` as a static website. The page states that the workshop is proposed and subject to acceptance. Replace those statements only after acceptance is confirmed.

For GitHub Pages, publish the `main` branch and the `/docs` directory.

Public website: https://geometricbci.github.io/icra2027-matrix-manifolds/
