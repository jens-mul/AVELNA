"""No real supplier image or paid generation is used in these CI tests."""
import hashlib
import importlib.util
import tempfile
import unittest
from pathlib import Path

import numpy as np
from PIL import Image, ImageDraw


ROOT = Path(__file__).resolve().parents[2]
MODULE_FILE = ROOT / "creative-tools" / "render_truth.py"
spec = importlib.util.spec_from_file_location("avelna_render_truth", MODULE_FILE)
render_truth = importlib.util.module_from_spec(spec)
spec.loader.exec_module(render_truth)


class ProductTruthRenderTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.path = Path(self.tmp.name) / "synthetic-photo.png"
        self.image = Image.new("RGB", (800, 800), "white")
        d = ImageDraw.Draw(self.image)
        d.rounded_rectangle((26, 174, 771, 645), radius=32, fill=(226, 225, 224))
        d.line((80, 180, 140, 280, 255, 370), fill=(194, 191, 190), width=6, joint="curve")
        self.image.save(self.path)
        self.hash = hashlib.sha256(self.path.read_bytes()).hexdigest()

    def test_exact_rgb_preserved_and_bbox(self):
        product, (left,top,right,bottom) = render_truth.extract_source_pixels(self.path,self.hash)
        self.assertEqual(product.mode, "RGBA")
        self.assertTrue(20 <= left <= 35)
        self.assertTrue(170 <= top <= 185)
        self.assertTrue(765 <= right <= 780)
        self.assertTrue(635 <= bottom <= 655)
        expected = np.array(self.image.crop((left,top,right,bottom)).convert("RGB"))
        actual = np.array(product.convert("RGBA"))[:, :, :3]
        self.assertTrue(np.array_equal(expected,actual))

    def test_wrong_sha_rejected(self):
        with self.assertRaises(ValueError):
            render_truth.extract_source_pixels(self.path,"0"*64)

    def test_gallery_sheet_exists_and_no_product_mutation(self):
        product,_=render_truth.extract_source_pixels(self.path,self.hash)
        diagram=render_truth.make_dimensions_sheet(product,600,390)
        self.assertEqual(diagram.size,(1800,1400))
        self.assertEqual(diagram.mode,"RGB")


if __name__ == "__main__":
    unittest.main()
