"""Guard the founder-approved Palette 04 token contract (no network access)."""

import json
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
TOKEN_FILE = ROOT / "config" / "brand.tokens.json"

LOCKED_COLORS = {
    "alabaster": "#F5F2EC",
    "stone": "#D4C9BC",
    "sage_grey": "#9DA08E",
    "olive_smoke": "#7C806E",
    "deep_mineral": "#31332F",
}


def relative_luminance(hex_color):
    rgb = [int(hex_color[i:i + 2], 16) / 255 for i in (1, 3, 5)]
    channels = [
        channel / 12.92 if channel <= 0.04045 else ((channel + 0.055) / 1.055) ** 2.4
        for channel in rgb
    ]
    return sum(a * b for a, b in zip(channels, (0.2126, 0.7152, 0.0722)))


def contrast_ratio(foreground, background):
    light, dark = sorted(
        (relative_luminance(foreground), relative_luminance(background)),
        reverse=True,
    )
    return (light + 0.05) / (dark + 0.05)


class BrandPaletteTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.tokens = json.loads(TOKEN_FILE.read_text(encoding="utf-8"))

    def test_palette_04_is_explicitly_locked(self):
        self.assertEqual(self.tokens["schema_version"], 2)
        self.assertEqual(self.tokens["palette_lock"]["id"], "olive-mineral-04")
        self.assertEqual(self.tokens["palette_lock"]["status"], "locked")
        self.assertEqual(self.tokens["palette_lock"]["color_space"], "sRGB")
        self.assertEqual(self.tokens["palette_lock"]["approved_date"], "2026-11-01")
        self.assertEqual(self.tokens["version"], "1.1.0")

    def test_exact_canonical_colors(self):
        self.assertEqual(self.tokens["colors"], LOCKED_COLORS)

    def test_semantic_roles_only_resolve_into_locked_palette(self):
        colors = self.tokens["colors"]
        semantic = self.tokens["semantic_colors"]
        for name, target in semantic.items():
            with self.subTest(role=name):
                self.assertIn(target, colors)
        self.assertEqual(semantic["text_primary"], "deep_mineral")
        self.assertEqual(semantic["primary_cta_background"], "deep_mineral")
        self.assertEqual(semantic["primary_cta_text"], "alabaster")
        self.assertEqual(semantic["identity_accent"], "olive_smoke")

    def test_regular_text_and_cta_default_pass_aa(self):
        colors = self.tokens["colors"]
        roles = self.tokens["semantic_colors"]
        safe_pairs = (
            (roles["text_primary"], roles["page_background"]),
            (roles["text_primary"], roles["section_surface"]),
            (roles["primary_cta_text"], roles["primary_cta_background"]),
            (roles["text_on_dark"], "deep_mineral"),
        )
        for foreground, background in safe_pairs:
            with self.subTest(foreground=foreground, background=background):
                self.assertGreaterEqual(
                    contrast_ratio(colors[foreground], colors[background]), 4.5
                )

    def test_muted_accents_are_not_default_small_text(self):
        colors = self.tokens["colors"]
        self.assertLess(contrast_ratio(colors["olive_smoke"], colors["alabaster"]), 4.5)
        self.assertLess(contrast_ratio(colors["sage_grey"], colors["alabaster"]), 4.5)
        self.assertNotIn(
            self.tokens["semantic_colors"]["text_primary"],
            {"olive_smoke", "sage_grey"},
        )

    def test_photo_direction_is_not_second_brand_palette(self):
        photography = self.tokens["photography"]
        self.assertTrue(photography["not_brand_palette"])
        self.assertIn("Sand & Linen", photography["direction"])
        reference = ROOT / photography["environment_reference"]
        self.assertTrue(reference.is_file(), f"Missing approved reference: {reference}")
        self.assertTrue((ROOT / self.tokens["palette_lock"]["specification"]).is_file())


if __name__ == "__main__":
    unittest.main()
