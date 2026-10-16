import math
NUMCOL={1:"#E53935",2:"#FB8C00",3:"#FDD835",4:"#43A047",5:"#1E88E5",6:"#8E24AA",7:"#8E24AA",8:"#EC407A",9:"#9E9E9E",10:"#E53935"}
INK="#272650"
# finger specs for a RIGHT hand, palm facing viewer, thumb on left. (cx, base_y, length, width, angle)
# order raised: index, middle, ring, pinky, thumb
F={ "index":(46,0.0), "middle":(66,0), "ring":(86,0), "pinky":(104,0) }
def hand(kind, up, col, mirror=False, dots=None, scale=1.0, start=0):
    """up = number of raised fingers 0..5 (order index,middle,ring,pinky,thumb). returns svg group, width 140 h 150"""
    order=["index","middle","ring","pinky","thumb"]
    raised=set(order[:up])
    g=[]
    W=15; 
    lens={"index":58,"middle":66,"ring":58,"pinky":44}
    xs={"index":47,"middle":67,"ring":87,"pinky":105}
    base=88
    fill_up=col; fill_dn="#ffffff" if kind=="B" else "#E8E9F5"
    stroke=INK
    sw=3
    palm_fill = col if kind in("A","C") else "#F4F5FB"
    if kind=="A": palm_fill=col
    if kind=="B": palm_fill="#ffffff"
    if kind=="B2": palm_fill = col if up==5 else "#ffffff"
    if kind=="C": palm_fill="#ffffff"
    if kind=="D": palm_fill=None
    # palm
    # fingers
    for k in ["index","middle","ring","pinky"]:
        x=xs[k]; L=lens[k]
        isup = k in raised
        if kind=="D":
            h = L if isup else 14
            f = col if isup else "#E8E9F5"
            g.append(f'<rect x="{x-W/2}" y="{base+30-h}" width="{W}" height="{h}" rx="{W/2}" fill="{f}" stroke="{stroke}" stroke-width="{sw}"/>')
            continue
        if isup:
            ff = col if kind in ("A","B","B2") else "#ffffff"
            if kind in ("B","B2"): ff=col
            g.append(f'<rect x="{x-W/2}" y="{base-L}" width="{W}" height="{L+10}" rx="{W/2}" fill="{ff}" stroke="{stroke}" stroke-width="{sw}"/>')
            if kind=="C" and dots is not None:
                pass
        else:
            if kind=="A":
                g.append(f'<rect x="{x-W/2}" y="{base-14}" width="{W}" height="30" rx="{W/2}" fill="{col}" stroke="{stroke}" stroke-width="{sw}"/>')
            elif kind in ("B","B2"):
                g.append(f'<rect x="{x-W/2}" y="{base-14}" width="{W}" height="30" rx="{W/2}" fill="#ffffff" stroke="{stroke}" stroke-width="{sw}"/>')
            elif kind=="C":
                g.append(f'<rect x="{x-W/2}" y="{base-14}" width="{W}" height="30" rx="{W/2}" fill="#ffffff" stroke="{stroke}" stroke-width="{sw}"/>')
    # thumb
    tup = "thumb" in raised
    if kind=="D":
        h=40 if tup else 14
        f=col if tup else "#E8E9F5"
        g.append(f'<rect x="12" y="{base+30-h}" width="{W+3}" height="{h}" rx="{(W+3)/2}" fill="{f}" stroke="{stroke}" stroke-width="{sw}"/>')
    else:
        ang=-28 if tup else 62
        ln=46 if tup else 26
        ff = col if kind in ("A","B","B2") else "#ffffff"
        if not tup:
            if kind=="A": ff=col
            if kind in ("B","B2"): ff="#ffffff"
            if kind=="C": ff="#ffffff"
        op = 1
        dash = '' if (tup or kind!="B") else 'stroke-dasharray="3 5"'
        g.append(f'<g transform="translate(40,112) rotate({ang})"><rect x="-{W/2+1}" y="-{ln}" width="{W+2}" height="{ln+6}" rx="{(W+2)/2}" fill="{ff}" stroke="{stroke}" stroke-width="{sw}" {dash} opacity="{op}"/></g>')
        # cover base of thumb joining palm
    # redraw palm top edge over finger bases for A/B/C for clean join (not needed visually)
    if kind!="D":
        g.append(f'<rect x="34" y="70" width="86" height="64" rx="26" fill="{palm_fill}" stroke="{stroke}" stroke-width="{sw}"/>')
    # fingertip number dots (option C)
    labels=[]
    if kind=="C":
        n=start
        for k in ["index","middle","ring","pinky"]:
            if k in raised:
                n+=1; labels.append((xs[k], base-lens[k]+11, n))
        if tup:
            n+=1; labels.append((23.6, 81.1, n))
    for (x,y,t) in labels:
        xx = 154-x if mirror else x
        g.append(f'<circle cx="{xx}" cy="{y}" r="9" fill="{col}" stroke="{INK}" stroke-width="2.5" class="LBL"/><text x="{xx}" y="{y+5}" text-anchor="middle" font-family="Figtree" font-weight="700" font-size="14" fill="{INK}" class="LBL">{t}</text>')
    shapes="".join(x for x in g if "LBL" not in x)
    lbls="".join(x for x in g if "LBL" in x)
    body=shapes
    if mirror:
        body=f'<g transform="translate(154,0) scale(-1,1)">{body}</g>'

    return body+lbls

def fingers(kind,n):
    col=NUMCOL[n]
    if n<=5:
        return f'<svg viewBox="0 0 154 160" width="170">{hand(kind,n,col)}</svg>'
    return f'<svg viewBox="0 0 330 160" width="330">{hand(kind,5,NUMCOL[5])}<g transform="translate(176,0)">{hand(kind,n-5,NUMCOL[n-5] if n<10 else NUMCOL[5],mirror=True,start=5)}</g></svg>'

opts=[("B","Now: ghost hands, palm stays white","Only the raised fingers take the colour, even when all five are up."),
      ("B2","Your idea: full hand fills in","When all five fingers are up, the whole hand fills with the colour of 5. It reads as one solid block of five.")]
html='''<html><head><style>
@font-face{font-family:Figtree;font-weight:400;src:url('file:///home/claude/dino-gang/public/fonts/figtree-latin-400-normal.woff2')}
@font-face{font-family:Figtree;font-weight:700;src:url('file:///home/claude/dino-gang/public/fonts/figtree-latin-700-normal.woff2')}
body{margin:0;background:#f4f5fb;font-family:Figtree,sans-serif;color:#272650;padding:22px;width:1500px}.pair{flex-wrap:wrap}
h1{margin:0 0 14px;font-size:26px}
.row{display:grid;grid-template-columns:1fr;gap:16px}
.card{background:#fff;border:2px solid #e0e2f0;border-radius:22px;padding:16px 18px}
.card h2{margin:0;font-size:21px}.card p{margin:2px 0 8px;color:#55587f;font-size:15px}
.pair{display:flex;gap:26px;align-items:flex-end;justify-content:center;background:#f9f9fe;border-radius:16px;padding:12px}
.lab{font-weight:700;text-align:center;font-size:15px;margin-top:2px}
</style></head><body><h1>Ghost hands: full hand fill</h1><div class="row">'''
for k,t,d in opts:
    html+=f'<div class="card"><h2>{k}. {t}</h2><p>{d}</p><div class="pair">'+"".join(f'<div>{fingers(k,n)}<div class="lab">{n}</div></div>' for n in (3,5,8,10))+'</div></div>'
html+='</div><script>document.querySelectorAll("g[transform^=\\\"translate(154\"] text.dg").forEach(function(t){var x=t.getAttribute("x");var p=t.getAttribute("transform")||"";t.setAttribute("transform",p+" translate("+x+" 0) scale(-1 1) translate("+(-x)+" 0)")})</script></body></html>'
open("opts.html","w").write(html)
