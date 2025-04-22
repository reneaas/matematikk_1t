import turtle
import imageio.v2 as imageio  # v2 API = no deprecation warnings
from PIL import Image  # pillow >=10
import io, os, shutil, natsort

# --- Animation Control -------------------------------------------------------
running = True
FPS = 60
turtle.speed(8)
frames = []  # full paths of *.png frames


def stop():  # stop the capture loop
    global running
    running = False


# -----------------------------------------------------------------------------
def save(counter=[1]):
    turtle.update()
    """Grab the canvas, convert white→transparent, save PNG into temp_frames/"""
    # 1. PostScript dump -> Pillow Image
    ps = (
        turtle.getcanvas()
        .postscript(colormode="color", x=-200, y=-150, width=400, height=300)
        .encode("utf-8")
    )
    img = Image.open(io.BytesIO(ps)).convert("RGBA")

    # 2. White ➜ transparent
    datas = [
        (*px[:3], 0) if px[:3] == (255, 255, 255) else px  # turn pure‑white α=0
        for px in img.getdata()
    ]
    img.putdata(datas)

    # 3. Store as PNG
    fname = os.path.join("temp_frames", f"frame_{counter[0]}.png")
    img.save(fname, "PNG")
    frames.append(fname)

    counter[0] += 1
    if running:
        turtle.ontimer(save, int(1000 / FPS))


# --- Assemble GIF ------------------------------------------------------------
def make_gif(out_name, src_frames):
    imgs = [imageio.imread(f) for f in src_frames]
    imageio.mimsave(
        out_name,
        imgs,
        duration=1 / FPS,
        loop=0,  # 0 = infinite loop
        subrectangles=True,  # smaller GIF, keeps transparency
        disposal=2,
    )


# --- Drawing -----------------------------------------------------------------
def draw():
    turtle.forward(100)
    turtle.left(90)

    turtle.forward(100)
    turtle.left(90)

    turtle.forward(100)
    turtle.left(90)

    turtle.forward(100)
    turtle.right(90)

    turtle.forward(100)
    turtle.right(90)

    turtle.forward(100)
    turtle.right(90)

    turtle.forward(100)
    turtle.right(90)

    turtle.ontimer(stop, 1000)  # Stop recording after 1 second


# -----------------------------------------------------------------------------
if __name__ == "__main__":
    # 0. Prep
    os.makedirs("temp_frames", exist_ok=True)
    # turtle.tracer(False)  # speed up drawing (optional)

    # 1. Start capture + drawing
    save()
    turtle.ontimer(draw, 500)
    turtle.done()

    # 2. Sort frames and build GIF
    frames_sorted = natsort.natsorted(frames)
    out_gif = os.path.splitext(__file__)[0] + ".gif"
    make_gif(out_gif, frames_sorted)

    # 3. Clean up
    shutil.rmtree("temp_frames")
    print("Saved transparent gif ➜", out_gif)
