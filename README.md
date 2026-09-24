# MERV — Measuring Renewables Uptake & Value

Project website for **MERV (Measuring Renewables Uptake & Value)**, an 18-month ESRC-funded project (grant reference UKRI5675) led by Prof Nick Bailey at the Urban Big Data Centre, University of Glasgow, with Prof David McArthur, Prof Qunshan Zhao and Dr Michail Georgiou.

Built from the same template as the [AGILE PhD School 2026 site](https://urbanbigdatacentre.github.io/agilephdschool2026/) (R distill look: white fixed navbar, `#1277A7` links, floating table of contents, `#0F2E3D` dark footer) — a plain static site with no build tools. Edit [index.html](index.html) for content and [style.css](style.css) for styling, then push.

## Structure

Single page with anchor sections (linkable, e.g. `…/#outputs`):

| Anchor | Content |
|---|---|
| `#overview` | Why it matters, the challenge (uptake figures), research questions, five objectives, indicative timeline, applications and benefits |
| `#team` | Investigators (linked to their UBDC profiles) and partners/stakeholders |
| `#outputs` | Papers, data, code, policy briefs and reports, related earlier work |
| `#news` | Dated one-line news items (same table style as the AGILE programme) |
| `#funding` | ESRC / UBDC / University of Glasgow logos, grant number, contact, CC BY notice |

The green vacancy box near the top (`#vacancy`) advertises the Research Associate post, which closes on 6 October 2026 — remove or replace it after that date (and update the RA line in Team and the News table).

Draft placeholders are marked with a yellow `<span class="tbc">…</span>` tag — remove the span (and the `.tbc` rule in `style.css` if none are left) once the fact is confirmed.

## Images (`images/`)

- `ubdc_logo.svg` — from [ubdc.ac.uk](https://www.ubdc.ac.uk/) (navbar + funding logos).
- `glasgow_logo.png` — University of Glasgow logo, taken from the MERV project summary document.
- `esrc_logo.png` — UKRI / ESRC horizontal logo, from [Wikimedia Commons](https://commons.wikimedia.org/wiki/File:UKRI_ESR_Council-Logo_Horiz-RGB.png) (uploaded by UKRI). Replace with the official file from the UKRI brand pack if preferred.
- `hero-home-energy.svg` — hero illustration (house with solar PV, heat pump, home battery and EV charging), drawn for this site; CC BY 4.0 like the rest of the page. Edit the SVG directly to change colours or labels.
- `hero-solar-crickhowell.jpg` — alternative photographic hero (not currently used): rooftop solar panels on a house in Crickhowell, Wales, by Jaggery, [geograph.org.uk via Wikimedia Commons, CC BY-SA 2.0](https://commons.wikimedia.org/wiki/File:Rooftop_solar_panels,_New_Road,_Crickhowell_-_geograph.org.uk_-_7219809.jpg). If you switch to it, credit it in the figure caption.

## Content source

Text follows the MERV research project summary (Prof Nick Bailey, University of Glasgow). Figures quoted: heat pumps in ~2% of UK dwellings (EU 16%), clean heating ~9%, solar PV ~7% (EU 10%), batteries ~1%.

## Deployment

Intended to be served by GitHub Pages from the `main` branch of `urbanbigdatacentre/merv` (root path), i.e. at `https://urbanbigdatacentre.github.io/merv/`. Once the repository exists:

```bash
cd /Users/qzhao/Desktop/UBDC/MERV
git add -A
git commit -m "update"
git push
```

Pages redeploys automatically within a minute or two of each push.

## License

Text and figures: [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/). Photographs keep their own licences (see captions); funder and institution logos belong to their owners.
