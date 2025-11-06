# build_single_file.py
import json, sys, io

INDEX = "index_bundled.html"      # the HTML file I just added
OUT   = "index.html"
GRAF  = "GRAFIKS.csv"
DAL   = "DALIBNIEKI.csv"

def read_text(p):
    return io.open(p, "r", encoding="utf-8", errors="replace").read()

html = read_text(INDEX)
graf = read_text(GRAF)
dal  = read_text(DAL)

payload = {
    "mode": "csv-embedded",
    "grafiksCsv": graf,
    "dalibniekiCsv": dal
}

marker_start = '<script id="EMBEDDED_DATA" type="application/json">'
marker_end   = '</script>'

if marker_start not in html:
    sys.exit("Couldn't find EMBEDDED_DATA marker in index_bundled.html.")

start = html.index(marker_start) + len(marker_start)
end   = html.index(marker_end, start)
new_html = html[:start] + json.dumps(payload, ensure_ascii=False) + html[end:]

io.open(OUT, "w", encoding="utf-8").write(new_html)
print(f"✅ Wrote {OUT}. Double-click it (file://) and it will work offline.")
