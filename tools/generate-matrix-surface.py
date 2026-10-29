"""Draw the determinant-one SPD(2) surface in several illustration styles.

For P = [[z+x, y], [y, z-x]], use
  (x, y, z) = (sinh(r) cos(theta), sinh(r) sin(theta), cosh(r)).
Then det(P) = 1 and its eigenvalues are exp(+r), exp(-r).
The highlighted curve P(t) = exp(t S), for symmetric traceless S,
is a geodesic for the affine-invariant Riemannian metric.
Only the displayed projection is rotated and scaled; no data are implied.
"""
from math import sin, cos, sinh, cosh, pi, exp
from pathlib import Path
import argparse

parser = argparse.ArgumentParser(description=__doc__)
style = parser.add_mutually_exclusive_group()
style.add_argument('--illustrated', action='store_true', help='Use a sparse, stronger line drawing to accompany the cartoon robot.')
style.add_argument('--storybook', action='store_true', help='Add soft color blocks, a simple grid, and bold cartoon outlines to the analytic surface.')
options = parser.parse_args()
storybook = options.storybook
illustrated = options.illustrated or storybook

R = 1.9
ELEVATION = 34 * pi / 180
ROLL = -27 * pi / 180

def project(r, theta):
    x, y, z = sinh(r) * cos(theta), sinh(r) * sin(theta), cosh(r)
    assert abs(z*z-x*x-y*y-1) < 1e-12
    assert exp(-abs(r)) > 0
    u, v = x, sin(ELEVATION) * y - cos(ELEVATION) * z
    return u*cos(ROLL)-v*sin(ROLL), u*sin(ROLL)+v*cos(ROLL)

rim = [project(R, 2*pi*i/360) for i in range(361)]
mesh = [project(R*j/100, 2*pi*i/180) for j in range(101) for i in range(181)]
minx, maxx = min(p[0] for p in mesh), max(p[0] for p in mesh)
miny, maxy = min(p[1] for p in mesh), max(p[1] for p in mesh)
scale = min(428/(maxx-minx), 396/(maxy-miny))
mid = ((minx+maxx)/2, (miny+maxy)/2)

def mapped(p):
    return 250+(p[0]-mid[0])*scale, 228+(p[1]-mid[1])*scale

def path(points):
    return 'M'+' L'.join(f'{x:.2f},{y:.2f}' for x,y in map(mapped, points))

ring_count = 4 if storybook else 8 if illustrated else 22
meridian_count = 10 if storybook else 16 if illustrated else 36
line_color = '#718b65' if storybook else '#59766a' if illustrated else '#747c6d'
line_width = '3.2' if storybook else '1.5' if illustrated else '0.78'
parts = ['<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 500 480" fill="none">',
         '<title>Unit-determinant SPD(2) surface</title>',
         '<desc>A projected hyperboloid representing positive-definite two-by-two matrices of determinant one. A geodesic for the affine-invariant metric is drawn in red. The pastel coloring is decorative.</desc>']

if storybook:
    # Color the projected silhouette without perturbing the analytic grid.
    # Monotone-chain hull of the sampled projected surface.
    points = sorted(set(mesh))
    def cross(o, a, b):
        return (a[0]-o[0])*(b[1]-o[1])-(a[1]-o[1])*(b[0]-o[0])
    lower, upper = [], []
    for point in points:
        while len(lower) >= 2 and cross(lower[-2], lower[-1], point) <= 0:
            lower.pop()
        lower.append(point)
    for point in reversed(points):
        while len(upper) >= 2 and cross(upper[-2], upper[-1], point) <= 0:
            upper.pop()
        upper.append(point)
    silhouette = lower[:-1] + upper[:-1]
    outline = path(silhouette) + ' Z'
    parts.append(f'<path d="{outline}" fill="#d4e2c6" stroke="#566b52" stroke-width="6.5" stroke-linejoin="round"/>')
    inner = [project(R*.78, 2*pi*j/240) for j in range(241)]
    parts.append(f'<path d="{path(inner)} Z" fill="#f1f2db" opacity=".85"/>')

parts.append(f'<g stroke="{line_color}" stroke-width="{line_width}" stroke-linejoin="round" stroke-linecap="round">')

for i in range(1, ring_count):
    r = R*i/ring_count
    points = [project(r, 2*pi*j/240) for j in range(241)]
    opacity = .65+.15*i/ring_count if storybook else .48+.18*i/ring_count if illustrated else .38+.18*i/ring_count
    parts.append(f'<path d="{path(points)}" opacity="{opacity:.3f}"/>')

for i in range(meridian_count):
    theta = 2*pi*i/meridian_count
    points = [project(R*j/130, theta) for j in range(131)]
    opacity = .55 + .2*(1+sin(theta))/2 if storybook else (.45 if illustrated else .31) + .23*(1+sin(theta))/2
    parts.append(f'<path d="{path(points)}" opacity="{opacity:.3f}"/>')

parts.append('</g>')
parts.append(f'<path d="{path(rim)}" stroke="#535e4e" stroke-width="{5 if storybook else 1.8 if illustrated else 1.1}" opacity="{.9 if storybook else .75}"/>')

theta = .60
curve = [project(-R + 2*R*i/220, theta) for i in range(221)]
parts.append(f'<path d="{path(curve)}" stroke="#a54e36" stroke-width="{5.5 if storybook else 2.6 if illustrated else 1.8}" stroke-linecap="round"/>')
for point in [curve[0], curve[-1]]:
    x,y = mapped(point)
    parts.append(f'<circle cx="{x:.2f}" cy="{y:.2f}" r="{4.5 if storybook else 3}" fill="#a54e36"/>')
parts.append('</svg>')

filename = 'matrix-surface-storybook.svg' if storybook else 'matrix-surface-illustrated.svg' if illustrated else 'matrix-surface.svg'
target = Path(__file__).resolve().parents[1]/'docs/assets'/filename
target.write_text('\n'.join(parts)+'\n')
print(f'Generated {target.name}: {target.stat().st_size:,} bytes')
