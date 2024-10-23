import argparse
parser = argparse.ArgumentParser()
parser.add_argument("-i", required=True)
parser.add_argument("-o", required=True)
args = parser.parse_args()

import requests
with open(args.i, "r") as f:
    readme = f.read()

r = requests.post("https://api.github.com/markdown", json={"text": readme, "mode": "gfm"})

html = "<link href=\"https://unpkg.com/@primer/css@21.2.2/dist/primer.css\" rel=\"stylesheet\" />\n<div class=\"markdown-body\">\n" + r.text + "\n</div>"

with open(args.o, "w") as f:
    f.write(html)
