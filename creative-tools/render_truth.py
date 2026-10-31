#!/usr/bin/env python3
"""Generate source-pixel-locked top product images and a specification sheet.

This optional CLI has *no* image-generation provider integration.
It is tuned for the white-background, top-view VDSTM-007 reference and MUST NOT
be used on arbitrary photos without inspecting segmentation quality.
Requires Pillow, NumPy, OpenCV (see requirements.txt).
"""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path

import cv2
import numpy as np
from PIL import Image, ImageDraw, ImageFont, ImageFilter


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def extract_source_pixels(path: Path, expected_sha: str) -> tuple[Image.Image, tuple[int,int,int,int]]:
    if sha256(path) != expected_sha:
        raise ValueError("Input hash mismatch: source is not the approved photograph")
    im = Image.open(path).convert("RGB")
    if im.size != (800, 800):
        raise ValueError("Input size differs from the approved product source")
    rgb = np.array(im)
    brightness = cv2.cvtColor(rgb, cv2.COLOR_RGB2GRAY)
    binary = (brightness < 250).astype("uint8") * 255
    binary[:165] = 0
    binary[660:] = 0
    binary[:, :16] = 0
    binary[:, 782:] = 0
    count, labels, stats, _ = cv2.connectedComponentsWithStats(binary)
    if count < 2:
        raise ValueError("Product segmentation failed: no contour")
    label = 1 + int(np.argmax(stats[1:, cv2.CC_STAT_AREA]))
    largest = np.where(labels == label, 255, 0).astype("uint8")
    contours, _ = cv2.findContours(largest, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    contour = max(contours, key=cv2.contourArea)
    fill = np.zeros_like(largest)
    cv2.drawContours(fill, [contour], -1, 255, -1)
    mask = cv2.GaussianBlur(fill, (3, 3), 0.55)
    ys, xs = np.where(mask > 5)
    box = (int(xs.min()), int(ys.min()), int(xs.max()) + 1, int(ys.max()) + 1)
    if not (20 <= box[0] <= 35 and 170 <= box[1] <= 185 and
            765 <= box[2] <= 780 and 635 <= box[3] <= 655):
        raise ValueError("Unexpected bounding box: do not silently mask a new product")
    product = im.crop(box).convert("RGBA")
    product.putalpha(Image.fromarray(mask, "L").crop(box))
    return product, box


def get_font(size: int):
    fonts = [
        "/usr/share/fonts/opentype/inter/Inter-Medium.otf",
        "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf",
    ]
    for path in fonts:
        if Path(path).is_file():
            return ImageFont.truetype(path, size)
    return ImageFont.load_default()


def make_dimensions_sheet(product: Image.Image, width_mm: int, height_mm: int) -> Image.Image:
    W, H = 1800, 1400
    background = Image.new("RGBA", (W, H), "#F5F3EE")
    draw = ImageDraw.Draw(background)
    ink, muted, line = "#2F302D", "#77756D", "#CAC8C0"
    draw.text((110, 80), "AVELNA", fill=ink, font=get_font(40))
    draw.text((110, 205), "Precise proportions.", fill=ink, font=get_font(65))
    draw.text((110, 290), "VDSTM-007  |  SUPPLIER-DECLARED DIMENSIONS", fill=muted, font=get_font(25))
    draw.rounded_rectangle((110, 350, 1690, 1170), radius=28, fill="#FBFBF8")
    scale = min(1220 / product.width, 600 / product.height)
    resized = product.resize((round(product.width * scale), round(product.height * scale)), Image.Resampling.LANCZOS)
    x, y = (W - resized.width) // 2 + 60, 550 + (580-resized.height)//2
    sh = Image.new("RGBA", resized.size, (55, 55, 50, 0))
    sh.putalpha(resized.getchannel("A").point(lambda a: round(a * 0.13)))
    layer = Image.new("RGBA", (W,H))
    layer.alpha_composite(sh, (x+2, y+15))
    layer = layer.filter(ImageFilter.GaussianBlur(16))
    background.alpha_composite(layer)
    background.alpha_composite(resized, (x, y))
    draw = ImageDraw.Draw(background)
    # Dimensional annotations are deterministic text — not AI-generated labels.
    draw.line([(x, 472), (x+resized.width, 472)], fill=muted, width=2)
    for xx in (x, x+resized.width):
        draw.line([(xx, 461), (xx, 483)], fill=muted, width=2)
    label = f"{width_mm} mm"
    bb=draw.textbbox((0,0),label,font=get_font(32))
    draw.text((x+resized.width//2-(bb[2]-bb[0])//2, 425),label,font=get_font(32),fill=ink)
    left = x-135
    draw.line([(left,y),(left,y+resized.height)],fill=muted,width=2)
    for yy in (y,y+resized.height):
        draw.line([(left-11,yy),(left+11,yy)],fill=muted,width=2)
    draw.text((left-110,y+resized.height//2),f"{height_mm} mm",font=get_font(30),fill=ink)
    draw.line([(110,1235),(1690,1235)],fill=line,width=2)
    draw.text((110,1285),"THICKNESS: NOT VERIFIED",font=get_font(26),fill=ink)
    draw.text((1030,1285),"BACKING: NOT VERIFIED",font=get_font(26),fill=muted)
    return background.convert("RGB")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--source", required=True)
    parser.add_argument("--manifest", required=True)
    parser.add_argument("--out", required=True)
    args = parser.parse_args()
    m = json.loads(Path(args.manifest).read_text(encoding="utf8"))
    if m.get("state",{}).get("commercial_master_approved") is True:
        raise ValueError("This toolkit does not grant commercial product approval")
    product, bounds = extract_source_pixels(Path(args.source), m["source"]["sha256"])
    out=Path(args.out);out.mkdir(parents=True,exist_ok=True)
    product.save(out/"exact-source-pixel-cutout.png")
    product.resize((product.width*2,product.height*2),Image.Resampling.LANCZOS).save(out/"locked-top-reference-transparent.png")
    facts=m["product_facts"]
    sheet=make_dimensions_sheet(product,facts["long_side_mm"],facts["short_side_mm"])
    sheet.save(out/"supplier-declared-dimensions.png")
    report={
        "source_sha256": sha256(Path(args.source)),
        "bbox_px": bounds,
        "derived": {
            f.name: sha256(f)
            for f in out.iterdir() if f.is_file()
        },
        "sku":m.get("supplier_model"),
        "approval":"internal_reference_only",
    }
    (out/"render-report.json").write_text(json.dumps(report,indent=2)+"\n",encoding="utf8")
    print(json.dumps(report,indent=2))


if __name__ == "__main__":
    main()
