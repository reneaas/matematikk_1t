from svgutils.compose import Figure, SVG


def main(dirname):
    # Only using A and B figures now
    fignames = ["algebraisk_uttrykk_1.svg", "algebraisk_uttrykk_2.svg"]
    figure_paths = [dirname + "/" + figname for figname in fignames]
    svgs = [SVG(path) for path in figure_paths]

    svg_width = max(svg.width for svg in svgs)
    svg_height = max(svg.height for svg in svgs)

    fig = Figure(
        svg_width * 2,  # Total width for two figures side by side
        svg_height,  # Only one row height needed
        SVG(dirname + "/algebraisk_uttrykk_1.svg").scale(1.25).move(0, 0),
        SVG(dirname + "/algebraisk_uttrykk_2.svg").scale(1.25).move(svg_width, 0),
    )

    fig.save(dirname + "/merged_figure.svg")


if __name__ == "__main__":

    main(dirname=".")
