#!/usr/bin/env python3
"""
Export Instagram carousel slides as high-resolution PNGs.

Usage:
    python export_slides.py --input carousel.html --output slides/ --slides 7
"""

import argparse
import asyncio
from pathlib import Path

from playwright.async_api import async_playwright


VIEW_W = 420
VIEW_H = 525
TARGET_W = 1080
TARGET_H = 1350
SCALE = TARGET_W / VIEW_W


async def export_slides(input_html: Path, output_dir: Path, total_slides: int):
    """Export carousel slides as PNG images."""
    output_dir.mkdir(parents=True, exist_ok=True)

    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page(
            viewport={"width": VIEW_W, "height": VIEW_H},
            device_scale_factor=SCALE,
        )

        html_content = input_html.read_text(encoding="utf-8")
        await page.set_content(html_content, wait_until="networkidle")
        await page.wait_for_timeout(3000)

        # Hide Instagram frame chrome
        await page.evaluate("""() => {
            document.querySelectorAll('.ig-header,.ig-dots,.ig-actions,.ig-caption')
                .forEach(el => el.style.display = 'none');

            const frame = document.querySelector('.ig-frame');
            if (frame) {
                frame.style.cssText = 'width:420px;height:525px;max-width:none;border-radius:0;box-shadow:none;overflow:hidden;margin:0;';
            }

            const viewport = document.querySelector('.carousel-viewport');
            if (viewport) {
                viewport.style.cssText = 'width:420px;height:525px;aspect-ratio:unset;overflow:hidden;cursor:default;';
            }

            document.body.style.cssText = 'padding:0;margin:0;display:block;overflow:hidden;';
        }""")
        await page.wait_for_timeout(500)

        for i in range(total_slides):
            # Navigate to slide i
            await page.evaluate("""(idx) => {
                const track = document.querySelector('.carousel-track');
                if (track) {
                    track.style.transition = 'none';
                    track.style.transform = 'translateX(' + (-idx * 420) + 'px)';
                }
            }""", i)
            await page.wait_for_timeout(400)

            # Screenshot the slide
            output_path = output_dir / f"slide_{i+1}.png"
            await page.screenshot(
                path=str(output_path),
                clip={"x": 0, "y": 0, "width": VIEW_W, "height": VIEW_H}
            )
            print(f"Exported slide {i+1}/{total_slides}: {output_path}")

        await browser.close()

    print(f"\nExport complete! {total_slides} slides saved to {output_dir}")


def main():
    parser = argparse.ArgumentParser(description="Export Instagram carousel as PNG slides")
    parser.add_argument("--input", type=Path, required=True, help="Input HTML file")
    parser.add_argument("--output", type=Path, required=True, help="Output directory")
    parser.add_argument("--slides", type=int, required=True, help="Total number of slides")
    args = parser.parse_args()

    if not args.input.exists():
        print(f"Error: Input file not found: {args.input}")
        return 1

    asyncio.run(export_slides(args.input, args.output, args.slides))
    return 0


if __name__ == "__main__":
    exit(main())
