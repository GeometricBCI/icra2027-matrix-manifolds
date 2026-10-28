# Illustrated robot artwork

The active website uses a cartoon illustration with rounded cream links, muted sage joints, a small terracotta detail, and hand-drawn ink and gouache textures. The large serif typography and restrained page layout retain a formal research-event identity.

Created with the built-in imagegen tool in two edit passes on October 29, 2026. The first pass used `artwork/robot-arm.png` as its edit target; the second simplified the first pass. This is conceptual artwork, not a photograph or an equipment specification.

Final source: `artwork/robot-arm-illustrated.png`.
Website asset: `docs/assets/robot-arm-illustrated.webp`, encoded at quality 90 with the original alpha preserved.

The active matrix surface uses the original analytic SPD(2) parameterization with fewer mesh lines, a pastel fill, and soft outlines. Regenerate it with `python3 tools/generate-matrix-surface.py --storybook`; use `--illustrated` for the earlier sparse line drawing. The mathematical grid and highlighted geodesic remain analytically generated. Its juxtaposition with the robot is illustrative, not a specific kinematic mapping.

## First edit prompt

Use case: style-transfer.
Asset type: a refined, gently playful editorial spot illustration for a robotics research workshop website.
Input image: edit target — the existing isolated robot-arm image. Reinterpret it completely as a two-dimensional hand-drawn cartoon illustration while retaining its recognizable articulated-arm silhouette and overall pose.
Composition invariants: one complete robot arm, square transparent canvas, base in lower-right, elbow bending across upper-right, forearm reaching upper-left and a small two-finger gripper pointing downward-left. Keep the entire base, links, joints, and gripper visible, with clear empty space beneath the forearm and in the lower-left for a separate mathematical drawing. Do not add the mathematical drawing yourself.
Art direction: sophisticated illustrated science book / independent cultural magazine. Matte gouache color blocks, beautiful expressive charcoal-ink contours with slight natural variation, a few fine dry-pencil marks, sparing crosshatching in the joints. This must be visibly hand-drawn cartoon art, not a photograph, not a 3D render, not a glossy plastic toy. Make the proportions a little softer and more charming: rounded ivory links, plump circular joints, short rounded gripper fingers, a gently inquisitive bent pose. Keep the structure coherent and connected.
Palette: warm cream links, muted dusty sage-green joints, charcoal outlines, one or two tiny terracotta-red fasteners. Pale warm-gray flat shadows, very restrained grain inside colored areas. Flat paper-like materials, no realistic reflections, no glossy highlights. The friendly character should come from the shape and drawing; no human face, no eyes, no mouth.
Background: genuinely transparent alpha around the entire illustration, including the inner gap in the arm. Preserve transparent edges. No opaque paper rectangle, no vignette, no textured background, no floor or studio scene. A small hand-drawn grounding stroke below the base is acceptable.
Avoid: neon, gradients, smooth CGI shading, chrome, product photography, stock vector corporate style, emoji, stickers, sparkles, stars, floating icons, heart motifs, text, numbers, letters, logos, watermarks, fake equations, humans, additional objects, extra grippers, detached parts.
Output: one beautiful high-resolution square transparent illustration, clearly cartoon-like and quietly charming, refined enough for an academic research event.

## Final refinement prompt

Use case: style-transfer.
Edit target: this hand-drawn robot arm illustration.
Keep its exact overall square composition, base at lower-right, elbow arching over the top, gripper at upper-left pointing down, transparent background, cream / muted sage / tiny terracotta palette, and the vacant lower-left area.
Single refinement: make the drawing simpler, softer, and more cartoon-like, with a quietly cute character. Shorten and thicken the gripper's two fingers into rounded little pincers; use plump cream links and bold round sage joints. Remove at least two thirds of the small bolts, mechanical seams, metallic rings, and internal crosshatching. Reduce perspective detail and realistic shading into a few matte, flat gouache shadow shapes. Use charming hand-drawn charcoal contours that are confident and slightly irregular, with a subtle dry-paper texture only within color shapes. Keep the complete arm coherent and the joints connected. The arm should feel like a thoughtful illustration commissioned for a sophisticated cultural magazine, rather than an engineering rendering or a children's toy.
No human face, no eyes, no mouth, no stickers, no sparkles, no background, no equations, no text, no logos, no additional objects. Genuinely transparent alpha; keep all of the illustration comfortably within the canvas, with clear margins.
