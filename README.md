# MERV — Measuring Renewables Uptake & Value

Project website for **MERV (Measuring Renewables Uptake & Value)**, an 18-month ESRC-funded project (grant reference UKRI5675) led by Prof Nick Bailey at the Urban Big Data Centre, University of Glasgow, with Prof David McArthur, Prof Qunshan Zhao and Dr Michail Georgiou.

Built from the same template as the [AGILE PhD School 2026 site](https://urbanbigdatacentre.github.io/agilephdschool2026/) (R distill look: white fixed navbar, `#1277A7` links, floating table of contents, `#0F2E3D` dark footer) — a plain static site with no build tools. Edit [index.html](index.html) for content and [style.css](style.css) for styling, then push. When you change `style.css`, also bump the `?v=` query on the stylesheet link in `index.html` so browsers (GitHub Pages caches CSS for 10 minutes) pick up the new file.

Navigation: the fixed navbar carries the MERV logo (links home), the page sections (the one currently in view is underlined), UBDC and GitHub; on phones the sections collapse into the ☰ menu, which closes itself after a choice. There is no separate table of contents. A floating back-to-top button (bottom right) appears after scrolling past the hero; both behaviours live in the small script at the end of `index.html`.

## Structure

Single page with anchor sections (linkable, e.g. `…/#outputs`):

| Anchor | Content |
|---|---|
| (left gutter) | “At a glance” card (`<aside class="glance">`): ESRC logo, funder/grant, duration, lead, team, host, contact, vacancy link. Fixed in the left margin on screens ≥1250px, hidden otherwise — everything in it also appears in the page body. Update the dates and remove the vacancy line when they change. |
| `#overview` | Why it matters, the challenge (uptake figures), research questions, five objectives, indicative timeline, applications and benefits |
| `#team` | Investigators (linked to their UBDC profiles) and partners/stakeholders |
| `#outputs` | Papers, data, code, policy briefs and reports, related earlier work |
| `#news` | Dated one-line news items (same table style as the AGILE programme) |
| `#funding` | ESRC / UBDC / University of Glasgow logos, grant number, contact, CC BY notice |

The green vacancy box near the top (`#vacancy`) advertises the Research Associate post, which closes on 6 October 2026 — remove or replace it after that date (and update the RA line in Team and the News table).

Draft placeholders are marked with a yellow `<span class="tbc">…</span>` tag — remove the span (and the `.tbc` rule in `style.css` if none are left) once the fact is confirmed.

## Images (`images/`)

- `merv-logo.svg` — project logo (house with a solar-panel roof and rising bars + “MERV” wordmark), drawn for this site, CC BY 4.0; used in the navbar at 40px. `merv-icon.svg` is the icon alone, used as the favicon. The wordmark uses the system font stack, so it renders slightly differently across operating systems. (A version modelled on a colleague’s sketch — condensed “MERV” with a heat-pump house — was tried on 24 Sep 2026 and reverted; see commit `aa58fd8`.) When you replace either file, bump the `?v=` query on its reference in `index.html` so cached copies refresh.
- `ubdc_logo.svg` — from [ubdc.ac.uk](https://www.ubdc.ac.uk/) (navbar + funding logos).
- `glasgow_logo.png` — University of Glasgow logo, taken from the MERV project summary document.
- `esrc_logo.png` — UKRI / ESRC horizontal logo, from [Wikimedia Commons](https://commons.wikimedia.org/wiki/File:UKRI_ESR_Council-Logo_Horiz-RGB.png) (uploaded by UKRI). Replace with the official file from the UKRI brand pack if preferred.
- `photo-uk-house-solar.jpg` — rooftop solar on a UK house, by Watt A Lot, [Unsplash](https://unsplash.com/photos/a-house-with-solar-panels-gqpuuF3a2tY) ([Unsplash License](https://unsplash.com/license): free to use, credit given in the caption). One of the two hero photos (`.hero-pair`).
- `photo-heat-pump-uk.jpg` — air source heat pump beside a house near Cambridge, England, by Andrew Fogg, [Flickr via Wikimedia Commons, CC BY 2.0](https://commons.wikimedia.org/wiki/File:Fridge_in_reverse_(51398066663).jpg); resized to 1200 px. One of the two hero photos (`.hero-pair`); credit lives in the caption.
- `hero-solar-crickhowell.jpg` — alternative hero photo (not currently used): rooftop solar panels on a house in Crickhowell, Wales, by Jaggery, [geograph.org.uk via Wikimedia Commons, CC BY-SA 2.0](https://commons.wikimedia.org/wiki/File:Rooftop_solar_panels,_New_Road,_Crickhowell_-_geograph.org.uk_-_7219809.jpg). If you switch to it, credit it in the figure caption.

An illustrated hero (flat SVG of a house with solar PV, heat pump, battery and EV) was used briefly and removed on 24 Sep 2026; it can be restored from git history (commit `82f6b23`, `images/hero-home-energy.svg`).

## Title convention

The page title capitalises exactly the letters that form the acronym, as in the project summary: “**ME**asuring **R**enewables uptake & **V**alue (MERV)” — the acronym letters are also coloured blue (`.acro`). Keep “uptake” lower-case if you edit the title.

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
