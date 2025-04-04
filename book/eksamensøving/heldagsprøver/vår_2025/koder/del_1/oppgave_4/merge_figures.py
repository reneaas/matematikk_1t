from svgutils.compose import Figure, SVG


def main(dirname):

    fignames = [
        "graf_A.svg",
        "graf_B.svg",
        "graf_C.svg",
        "graf_D.svg",
        "graf_E.svg",
        "graf_F.svg",
    ]
    # figure_paths = [dirname + path for path in figure_paths]
    figure_paths = [dirname + "/" + figname for figname in fignames]
    svgs = [SVG(path) for path in figure_paths]

    svg_width = max(svg.width for svg in svgs)
    svg_height = max(svg.height for svg in svgs)

    fig = Figure(
        svg_width * 2,  # Total width for 2 columns
        svg_height * 3,  # Total height for 3 rows
        SVG(dirname + "/graf_A.svg").scale(1.25).move(0, 0),  # Top left
        SVG(dirname + "/graf_B.svg").scale(1.25).move(svg_width, 0),  # Top right
        SVG(dirname + "/graf_C.svg").scale(1.25).move(0, svg_height),  # Middle left
        SVG(dirname + "/graf_D.svg")
        .scale(1.25)
        .move(svg_width, svg_height),  # Middle right
        SVG(dirname + "/graf_E.svg").scale(1.25).move(0, 2 * svg_height),  # Bottom left
        SVG(dirname + "/graf_F.svg")
        .scale(1.25)
        .move(svg_width, 2 * svg_height),  # Bottom right
    )

    fig.save(dirname + "/merged_figure.svg")


if __name__ == "__main__":

    import pathlib

    # Get the directory where the script is located
    current_dir = str(pathlib.Path(__file__).resolve().parent)

    parts = current_dir.split("/")
    for i in range(len(parts)):
        if parts[~i] == "koder":
            parts[~i] = "figurer"
            break

    dirname = "/".join(parts)

    main(dirname=dirname)
