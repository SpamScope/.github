# MailXray · by SpamScope

This identity is based on the approved draft: an envelope, a red magnifying glass, and a graph of indicators. Both logos include the words “by SpamScope”; the favicon uses only the symbol.

## Ready-to-use files

- `svg/logo-horizontal.svg`: horizontal logo, 1200 × 340.
- `svg/logo-stacked.svg`: stacked logo, 760 × 650.
- `svg/favicon.svg`: scalable symbol without highlights.
- `svg/favicon-small.svg`: simplified two-node variant for 16 px.
- `png/`: transparent logos at standard and double resolution; favicons at 16, 32, 48, 180, 192, 256, and 512 px.
- `favicon.ico`: 16, 32, 48, and 256 px sizes in one file.
- `previews/`: previews on white or dark backgrounds; use the transparent files for production.

The SVGs use paths and have no font, embedded image, or external dependencies. The SVG and PNG files have transparent backgrounds. Use the standard variants on white or very light backgrounds to keep the envelope and dark lettering legible.

## Dark backgrounds

Use `svg/logo-horizontal-dark.svg` or `svg/logo-stacked-dark.svg` on dark backgrounds. Their PNG equivalents are in `png/`, including `@2x` exports. These files have transparent backgrounds; the dark background appears only in the previews.

The envelope and dark lettering become white (`#FFFFFF`). The SpamScope red and lens blue remain unchanged. Connections inside the pale blue lens stay dark to preserve their contrast.

`svg/favicon-dark.svg`, `svg/favicon-small-dark.svg`, the `png/favicon-dark-*.png` files, and `favicon-dark.ico` provide matching symbols for dark backgrounds. The small SVG and 16 px PNG use two nodes for clarity.

## Palette

Colors sampled from the official logo in `branding/spamscope.png`:

| Color | Value | Use |
| --- | --- | --- |
| SpamScope red | `#FF0000` | Magnifying glass, nodes, Xray, and Spam |
| SpamScope dark | `#240000` | Envelope, connections, Mail, and Scope |
| Lens blue | `#D4F0FC` | Magnifying glass lens |
| White | `#FFFFFF` | Lens highlights in the logos |

## Sources and regeneration

The initial draft was created with image generation. The final files were redrawn using vector geometry and flat colors. The lettering uses outlines derived from Arial Rounded MT Bold and Avenir Next Regular; these fonts are not needed to view or use the exported logos.

`src/approved-draft.png` retains the approved proposal. `src/build.py` and `src/lettering.json` generate the SVG files. `src/export.py` produces PNG and ICO files using ImageMagick. `src/lettering.swift` can regenerate the lettering outlines on macOS.

From the `branding/mailxray` directory:

```sh
python3 src/build.py
python3 src/export.py
```

This package does not automatically modify or integrate with the backend or frontend repositories.

## Usage and rights

The [branding usage notice](../README.md#usage-and-rights) applies to these assets. Font names are mentioned for attribution; the exported outlines do not grant a license to the original fonts.
