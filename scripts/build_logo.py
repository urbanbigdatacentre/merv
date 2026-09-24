import math
from fontTools.ttLib import TTFont, TTCollection
from fontTools.pens.svgPathPen import SVGPathPen
from fontTools.pens.transformPen import TransformPen
from fontTools.pens.boundsPen import BoundsPen

NAVY = "#0f2e3d"
def load(path, face=None):
    if path.endswith(".ttc"):
        for f in TTCollection(path).fonts:
            if f["name"].getDebugName(4) == face: return f
        raise SystemExit("face not found " + face)
    return TTFont(path)
def cap_height(font):
    gs = font.getGlyphSet(); cmap = font.getBestCmap(); bp = BoundsPen(gs); gs[cmap[ord("H")]].draw(bp); return bp.bounds[3]
def text_path(font, text, x, baseline, scale, tracking=0.0):
    gs = font.getGlyphSet(); cmap = font.getBestCmap(); hmtx = font["hmtx"]; pen = SVGPathPen(gs); cx = x
    for ch in text:
        g = cmap[ord(ch)]; gs[g].draw(TransformPen(pen, (scale, 0, 0, -scale, cx, baseline))); cx += hmtx[g][0] * scale + tracking
    return pen.getCommands(), cx - x - tracking
def text_width(font, text, scale, tracking=0.0):
    cmap = font.getBestCmap(); hmtx = font["hmtx"]
    return sum(hmtx[cmap[ord(c)]][0] * scale for c in text) + tracking * (len(text) - 1)

def icon(tx, ty, s=1.0):
    peak = (78, 24); rgt = (172, 96); lft = (6, 96)
    dx, dy = rgt[0]-peak[0], rgt[1]-peak[1]; L = math.hypot(dx, dy); ux, uy = dx/L, dy/L
    nx, ny = uy, -ux
    ang = math.degrees(math.atan2(dy, dx))
    px, py = peak[0] + ux*4 + nx*13, peak[1] + uy*4 + ny*13
    cells = "".join(f'<rect x="{i*30}" y="-11" width="27" height="22" rx="4" fill="{NAVY}"/>' for i in range(3))
    return f'''<g transform="translate({tx},{ty}) scale({s})">
  <path d="M22,150 V92 M160,150 V92" fill="none" stroke="{NAVY}" stroke-width="13" stroke-linecap="round"/>
  <path d="M{lft[0]},{lft[1]} L{peak[0]},{peak[1]} L{rgt[0]},{rgt[1]}" fill="none" stroke="{NAVY}" stroke-width="13" stroke-linecap="round" stroke-linejoin="round"/>
  <g transform="translate({px:.1f},{py:.1f}) rotate({ang:.1f})">{cells}</g>
  <rect x="50" y="96" width="94" height="54" rx="7" fill="#cfe6e2" stroke="#87949c" stroke-width="3"/>
  <circle cx="97" cy="123" r="17.5" fill="#ffffff" stroke="{NAVY}" stroke-width="3.5"/>
  <path d="M97,123 C104,117 103,110 97,106.5 M97,123 C89,124 84,129 86,136 M97,123 C103,128 110,128 113,122" fill="none" stroke="{NAVY}" stroke-width="3.6" stroke-linecap="round"/>
  <circle cx="97" cy="123" r="4.2" fill="{NAVY}"/>
</g>'''

din = load("/System/Library/Fonts/Supplemental/DIN Condensed Bold.ttf")
tag = load("/System/Library/Fonts/Avenir Next Condensed.ttc", "Avenir Next Condensed Medium")
W = 600
s = 132.0 / cap_height(din)
d_word, w_word = text_path(din, "MERV", 12, 152, s, tracking=9)
TAG = "MEASURING RENEWABLES UPTAKE & VALUE"; n = len(TAG); trk = 0.8
ts = (566.0 - trk*(n-1)) / text_width(tag, TAG, 1.0, 0)
d_tag, w_tag = text_path(tag, TAG, 12, 210, ts, tracking=trk)
ico = icon(W - 188, 8)
def head(w, h): return f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" width="{w}" height="{h}" role="img" aria-label="MERV — Measuring Renewables Uptake and Value">'
open("merv-logo-full.svg", "w").write(head(W, 235) + f'\n<path d="{d_word}" fill="{NAVY}"/>\n{ico}\n<path d="{d_tag}" fill="{NAVY}"/>\n</svg>\n')
open("merv-logo.svg", "w").write(head(W, 165) + f'\n<path d="{d_word}" fill="{NAVY}"/>\n{ico}\n</svg>\n')
open("merv-icon.svg", "w").write('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 180 162" width="180" height="162" role="img" aria-label="MERV">\n' + icon(0, 6) + '\n</svg>\n')
print("word width", round(w_word), "tag width", round(w_tag))
