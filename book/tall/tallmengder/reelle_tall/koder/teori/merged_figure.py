from svgutils.compose import Figure, SVG


def main(dirname):
    # Only using A and B figures now
    fignames = ["teori_2.svg", "teori_3.svg"]
    figure_paths = [dirname + "/" + figname for figname in fignames]
    svgs = [SVG(path) for path in figure_paths]

    svg_width = max(svg.width for svg in svgs)
    svg_height = max(svg.height for svg in svgs)

    fig = Figure(
        svg_width,  # Total width for two figures side by side
        svg_height * 2.2,  # Only one row height needed
        SVG(dirname + "/teori_2.svg").scale(1.25).move(0, 0),
        SVG(dirname + "/teori_3.svg").scale(1.25).move(0, svg_height),
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
