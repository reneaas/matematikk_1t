import os
import cairosvg
import imageio.v2 as imageio
from pathlib import Path
from PIL import Image


def create_gif_from_svgs(svg_dir, output_name="faktortre.gif", duration=1.0):
    svg_dir = Path(svg_dir)
    svg_files = sorted(svg_dir.glob("step_*.svg"))

    if not svg_files:
        print("No SVG files found.")
        return

    png_files = []

    # Convert SVG to PNG with transparent background
    for svg in svg_files:
        png_path = svg.with_suffix(".png")
        cairosvg.svg2png(url=str(svg), write_to=str(png_path))
        png_files.append(png_path)

    frames = []
    for png_path in png_files:
        im = Image.open(png_path).convert("RGBA")

        # Force binary alpha: transparent or fully opaque
        new_data = []
        for pixel in im.getdata():
            if pixel[3] > 128:
                new_data.append(pixel)
            else:
                new_data.append((255, 255, 255, 0))
        im.putdata(new_data)

        # Convert to P mode with adaptive palette
        palette_img = im.convert("P", palette=Image.ADAPTIVE)
        transparent_index = palette_img.getpixel((0, 0))
        palette_img.info["transparency"] = transparent_index

        frames.append(palette_img)

    gif_path = svg_dir / output_name
    frames[0].save(
        gif_path,
        save_all=True,
        append_images=frames[1:],
        optimize=False,
        duration=int(duration * 1000),
        loop=0,
        transparency=frames[0].info["transparency"],
        disposal=2,
    )

    print(f"✅ Transparent GIF saved to: {gif_path}")

    # Optional cleanup of PNGs
    for png in png_files:
        png.unlink()


if __name__ == "__main__":
    # Replace with your actual figure directory
    current_dir = Path(__file__).resolve().parent
    fig_dir = current_dir.parent / "figurer"
    create_gif_from_svgs(".", duration=3)  # Adjust duration as desired
