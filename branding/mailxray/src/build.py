"""Build outlined SVG assets from the approved MailXray concept."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
LETTERS = json.loads((ROOT / 'src/lettering.json').read_text())
RED, INK, BLUE = '#FF0000', '#240000', '#D4F0FC'


def lettering(parts, size, x, baseline, centered=False):
    scale = size / 100
    width = sum(LETTERS[word]['width'] for word, _ in parts) * scale
    if centered:
        x -= width / 2
    paths = []
    for word, color in parts:
        paths.append(f'<path fill="{color}" transform="translate({x:.3f} {baseline}) scale({scale})" d="{LETTERS[word]["path"]}"/>')
        x += LETTERS[word]['width'] * scale
    return ''.join(paths)


def symbol(simple=False, tiny=False):
    # Open contours leave transparent clearance around the foreground lens.
    result = f'''<g fill="none" stroke="{INK}" stroke-width="16" stroke-linecap="round" stroke-linejoin="round"><path d="M121 102H43Q24 102 24 121V243Q24 262 43 262H251Q270 262 270 243V220"/><path d="M29 119L143 201Q148 205 154 201L164 193M31 251L112 181M261 251L211 213"/></g>
    <path d="M283 172L330 220" fill="none" stroke="{RED}" stroke-width="29" stroke-linecap="round"/>
    <circle cx="224" cy="110" r="85" fill="{BLUE}" stroke="{RED}" stroke-width="16"/>
    '''
    if tiny:
        result += f'<path d="M197 131L241 88" stroke="{INK}" stroke-width="13" stroke-linecap="round"/><circle cx="197" cy="131" r="15" fill="{RED}"/><circle cx="241" cy="88" r="15" fill="{RED}"/>'
    else:
        result += f'<path d="M187 137L229 78L258 142Z" fill="none" stroke="{INK}" stroke-width="11" stroke-linejoin="round"/>'
        for x, y in [(187,137),(229,78),(258,142)]:
            result += f'<circle cx="{x}" cy="{y}" r="16" fill="{RED}"/>'
    if not simple:
        result += '<circle cx="188" cy="69" r="11" fill="white"/><circle cx="170" cy="90" r="5" fill="white"/>'
    return result


def svg(name, width, height, body, label):
    content = f'''<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}" role="img" aria-labelledby="title"><title id="title">{label}</title>{body}</svg>'''
    (ROOT / 'svg' / f'{name}.svg').write_text(content)
    return content


main = [('Mail', INK), ('Xray', RED)]
by = [('by ', INK), ('Spam', RED), ('Scope', INK)]
svg('logo-horizontal', 1200, 340,
    '<g transform="translate(22 17)">' + symbol() + '</g>'
    + lettering(main, 157, 405, 196)
    + lettering(by, 48, 409, 263), 'MailXray by SpamScope')
svg('logo-stacked', 760, 650,
    '<g transform="translate(191 24) scale(1.05)">' + symbol() + '</g>'
    + lettering(main, 137, 380, 463, True)
    + lettering(by, 47, 380, 542, True), 'MailXray by SpamScope')
svg('favicon', 360, 360, '<g transform="translate(0 28)">' + symbol(True) + '</g>', 'MailXray')
svg('favicon-small', 360, 360, '<g transform="translate(0 28)">' + symbol(True, True) + '</g>', 'MailXray')
