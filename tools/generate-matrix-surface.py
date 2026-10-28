"""Draw the determinant-one SPD(2) surface as an orthographic engraving.

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
parser.add_argument('--illustrated', action='store_true', help='Use a sparse, stronger line drawing to accompany the cartoon robot.')
illustrated = parser.parse_args().illustrated

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

ring_count = 8 if illustrated else 22
meridian_count = 16 if illustrated else 36
line_color = '#59766a' if illustrated else '#747c6d'
line_width = '1.5' if illustrated else '0.78'
parts = ['<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 500 480" fill="none">',
         '<title>Unit-determinant SPD(2) surface</title>',
         '<desc>A projected hyperboloid representing positive-definite two-by-two matrices of determinant one. A geodesic for the affine-invariant metric is drawn in red.</desc>',
         f'<g stroke="{line_color}" stroke-width="{line_width}" stroke-linejoin="round" stroke-linecap="round">']

for i in range(1, ring_count):
    r = R*i/ring_count
    points = [project(r, 2*pi*j/240) for j in range(241)]
    parts.append(f'<path d="{path(points)}" opacity="{.48+.18*i/ring_count if illustrated else .38+.18*i/ring_count:.3f}"/>')

for i in range(meridian_count):
    theta = 2*pi*i/meridian_count
    points = [project(R*j/130, theta) for j in range(131)]
    opacity = (.45 if illustrated else .31) + .23*(1+sin(theta))/2
    parts.append(f'<path d="{path(points)}" opacity="{opacity:.3f}"/>')

parts.append('</g>')
parts.append(f'<path d="{path(rim)}" stroke="#535e4e" stroke-width="{1.8 if illustrated else 1.1}" opacity=".75"/>')

theta = .60
curve = [project(-R + 2*R*i/220, theta) for i in range(221)]
parts.append(f'<path d="{path(curve)}" stroke="#a54e36" stroke-width="{2.6 if illustrated else 1.8}" stroke-linecap="round"/>')
for point in [curve[0], curve[-1]]:
    x,y = mapped(point)
    parts.append(f'<circle cx="{x:.2f}" cy="{y:.2f}" r="3" fill="#a54e36"/>')
parts.append('</svg>')

target = Path(__file__).resolve().parents[1]/'docs/assets'/('matrix-surface-illustrated.svg' if illustrated else 'matrix-surface.svg')
target.write_text('\n'.join(parts)+'\n')
print(f'Generated {target.name}: {target.stat().st_size:,} bytes')
