"""Build the Limit Break community promo scene from the template.

    python build.py

Reads : scene.src.html                            (template)
        assets/limit-break-logo.png                (inlined as a data URI)
        assets/fonts/BarlowCondensed-*.woff2
        assets/SmashCY Discord.png
        assets/SmashCY Twitter (1).png

Writes: join-our-community.html

The output is a single self-contained file — no external files, no network,
no CDN. Point an OBS Browser Source straight at it.

To change the wording or QR images, edit scene.src.html (or swap the files
in assets/) and re-run.
"""
import base64
import os

HERE = os.path.dirname(os.path.abspath(__file__))

TEMPLATE = os.path.join(HERE, "scene.src.html")
LOGO = os.path.join(HERE, "assets", "limit-break-logo.png")
FONT_DIR = os.path.join(HERE, "assets", "fonts")
DISCORD_QR = os.path.join(HERE, "assets", "SmashCY Discord.png")
TWITTER_QR = os.path.join(HERE, "assets", "SmashCY Twitter (1).png")

OUTPUT = os.path.join(HERE, "join-our-community.html")

WEIGHTS = ("700", "800", "900")


def data_uri(path, mime):
    with open(path, "rb") as fh:
        return "data:%s;base64,%s" % (mime, base64.b64encode(fh.read()).decode("ascii"))


def main():
    with open(TEMPLATE, encoding="utf-8") as fh:
        template = fh.read()

    for label, path in (("logo", LOGO), ("discord QR", DISCORD_QR), ("twitter QR", TWITTER_QR)):
        if not os.path.exists(path):
            raise SystemExit("missing %s: %s" % (label, path))

    template = template.replace("__LOGO_DATA_URI__", data_uri(LOGO, "image/png"))
    template = template.replace("__DISCORD_QR_DATA_URI__", data_uri(DISCORD_QR, "image/png"))
    template = template.replace("__TWITTER_QR_DATA_URI__", data_uri(TWITTER_QR, "image/png"))

    for weight in WEIGHTS:
        path = os.path.join(FONT_DIR, "BarlowCondensed-%s.woff2" % weight)
        if not os.path.exists(path):
            raise SystemExit("missing font: " + path)
        template = template.replace("__FONT_%s__" % weight, data_uri(path, "font/woff2"))

    with open(OUTPUT, "w", encoding="utf-8") as fh:
        fh.write(template)

    print("%-26s %6.0f KB" % (os.path.basename(OUTPUT), os.path.getsize(OUTPUT) / 1024))


if __name__ == "__main__":
    main()
