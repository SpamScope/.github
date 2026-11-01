"""Export SVG masters with ImageMagick; package a multiresolution favicon."""
from pathlib import Path
import subprocess
import struct

ROOT = Path(__file__).resolve().parents[1]

def convert(*args):
    subprocess.run(['magick', *map(str, args)], check=True)

for name in ['logo-horizontal', 'logo-stacked']:
    convert('-background', 'none', ROOT/'svg'/f'{name}.svg', ROOT/'png'/f'{name}.png')
    convert('-background', 'none', '-density', '192', ROOT/'svg'/f'{name}.svg', ROOT/'png'/f'{name}@2x.png')
for size in [16, 32, 48, 180, 192, 256, 512]:
    source = 'favicon-small' if size == 16 else 'favicon'
    convert('-background', 'none', '-density', '384', ROOT/'svg'/f'{source}.svg', '-resize', f'{size}x{size}', ROOT/'png'/f'favicon-{size}.png')
(ROOT/'png/favicon.png').write_bytes((ROOT/'png/favicon-512.png').read_bytes())
sizes = [16, 32, 48, 256]
blobs = [(ROOT/'png'/f'favicon-{size}.png').read_bytes() for size in sizes]
offset = 6 + 16 * len(sizes)
entries = []
for size, blob in zip(sizes, blobs):
    entries.append(struct.pack('<BBBBHHII', size % 256, size % 256, 0, 0, 1, 32, len(blob), offset))
    offset += len(blob)
(ROOT/'favicon.ico').write_bytes(struct.pack('<HHH', 0, 1, len(sizes)) + b''.join(entries) + b''.join(blobs))
for name in ['logo-horizontal', 'logo-stacked']:
    convert(ROOT/'png'/f'{name}.png', '-background', 'white', '-alpha', 'remove', ROOT/'previews'/f'{name}-white.png')
convert(ROOT/'png/favicon-32.png', '-filter', 'point', '-resize', '256x256', '-background', 'white', '-alpha', 'remove', ROOT/'previews/favicon-32-enlarged.png')
