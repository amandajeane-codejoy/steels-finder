"""Rebuild index.html from the files in src/. Run: python3 build.py"""
from pathlib import Path
s = Path(__file__).parent / "src"
t = (s / "template.html").read_text()
out = (t.replace("__RAW__", (s / "raw_data.txt").read_text())
        .replace("__TAGS__", (s / "tags_final.txt").read_text())
        .replace("__PDF__", (s / "pdf_data.txt").read_text())
        .replace("__GLOSS__", (s / "glossary.js").read_text())
        .replace("__PEMAP__", (s / "pe_map.b64").read_text()))
body = "<!doctype html>\n<html lang=\"en\">\n<head>\n<meta charset=\"utf-8\">\n<meta name=\"viewport\" content=\"width=device-width, initial-scale=1, viewport-fit=cover\">\n<style>body{margin:0}img{max-width:100%}[hidden]{display:none!important}:root{padding-top:env(safe-area-inset-top,0px);padding-bottom:env(safe-area-inset-bottom,0px)}</style>\n"
# template starts with <title>, <meta>, <link>, <style>; place them in <head>, rest in <body>
split = out.index("</style>") + len("</style>")
html = body + out[:split] + "\n</head>\n<body>\n" + out[split:] + "\n</body>\n</html>\n"
(Path(__file__).parent / "index.html").write_text(html)
print("index.html rebuilt")
