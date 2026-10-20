"""Build the Bobby Dowza font: Andika (SIL OFL 1.1) with redrawn a e f i j l m n u y h d t.
Run: python3 tools/make-bobby-dowza.py   (needs fonttools, brotli, shapely)
Outputs public/fonts/bobbydowza-latin-{400,700}-normal.woff2 and LICENSE-BobbyDowza.txt."""
import json, os, shutil
from fontTools.ttLib import TTFont
from fontTools.svgLib.path import parse_path
from fontTools.pens.recordingPen import RecordingPen
from fontTools.pens.ttGlyphPen import TTGlyphPen
from shapely.geometry import LineString, Point
from shapely.ops import unary_union
from shapely.geometry.polygon import orient

R = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PATHS = json.load(open(os.path.join(R, "src/hw-paths.json"), encoding="utf-8"))
LETTERS = "aefijlmnuyhdt"
K = 17.4          # font units per path unit
BASE = 105        # path y that maps to the baseline
STROKE = {"400": 10.4, "700": 15.5}

def flat(d):
    pen = RecordingPen(); parse_path(d, pen)
    lines, cur = [], []
    for op, a in pen.value:
        if op == "moveTo":
            if len(cur) > 1: lines.append(cur)
            cur = [a[0]]
        elif op == "lineTo": cur.append(a[0])
        elif op == "curveTo":
            p0 = cur[-1]; p1, p2, p3 = a
            for i in range(1, 25):
                t = i / 24; u = 1 - t
                cur.append((u**3*p0[0]+3*u*u*t*p1[0]+3*u*t*t*p2[0]+t**3*p3[0], u**3*p0[1]+3*u*u*t*p1[1]+3*u*t*t*p2[1]+t**3*p3[1]))
    if len(cur) > 1: lines.append(cur)
    return lines

def outline(letter, sw):
    e = PATHS[letter]; parts = []
    for d in e["strokes"]:
        for ln in flat(d): parts.append(LineString(ln).buffer(sw/2, quad_segs=16))
    for (x, y) in e.get("dots", []): parts.append(Point(x, y).buffer(sw/2*0.95, quad_segs=16))
    return unary_union(parts)

def build(weight):
    src = os.path.join(R, "public/fonts/andika-latin-%s-normal.woff2" % weight)
    f = TTFont(src); cm = f.getBestCmap(); glyf = f["glyf"]; sw = STROKE[weight]
    for ch in LETTERS:
        gname = cm[ord(ch)]; old = glyf[gname]; lsb = min(max(old.xMin, 70), 100); rsb = 70
        geom = outline(ch, sw)
        minx = geom.bounds[0]
        polys = [geom] if geom.geom_type == "Polygon" else list(geom.geoms)
        pen = TTGlyphPen(None)
        for poly in polys:
            poly = orient(poly.simplify(0.04), sign=-1)  # outer clockwise
            for ring in [poly.exterior] + list(poly.interiors):
                pts = [(round((x - minx) * K + lsb), round((BASE - y) * K)) for x, y in list(ring.coords)[:-1]]
                pen.moveTo(pts[0])
                for p in pts[1:]: pen.lineTo(p)
                pen.closePath()
        g = pen.glyph(); glyf[gname] = g
        g.recalcBounds(glyf)
        adv = g.xMax + rsb
        f["hmtx"][gname] = (adv, g.xMin)
    fam = "Bobby Dowza"; sub = "Regular" if weight == "400" else "Bold"
    for n in f["name"].names:
        s = n.toUnicode()
        if n.nameID == 1: n.string = fam
        elif n.nameID == 2: n.string = sub
        elif n.nameID == 3: n.string = "BobbyDowza-%s-2026" % sub
        elif n.nameID == 4: n.string = "%s %s" % (fam, sub)
        elif n.nameID == 6: n.string = "BobbyDowza-%s" % sub
        elif n.nameID == 16: n.string = fam
        elif n.nameID == 17: n.string = sub
    f["name"].setName("Bobby Dowza is a modified version of Andika (SIL International) with redrawn a, e, f, i, j, m, n, u and y. Licensed under the SIL Open Font License 1.1.", 10, 3, 1, 0x409)
    out = os.path.join(R, "public/fonts/bobbydowza-latin-%s-normal.woff2" % weight)
    f.flavor = "woff2"; f.save(out); print(out, os.path.getsize(out))

for w in ("400", "700"): build(w)
shutil.copy(os.path.join(R, "public/fonts/LICENSE-Andika.txt"), os.path.join(R, "public/fonts/LICENSE-BobbyDowza.txt"))
