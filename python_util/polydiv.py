import os


def polylongdiv(
    fname: str, p: str, q: str, stage: int = None, svg: bool = True, vars=None
):
    if not vars:
        vars = "x"

    if stage is None:
        div_cmd = r"\polylongdiv[style=C, div=:, vars=None]{{p}}{{q}}"
        div_cmd = div_cmd.replace("{p}", p).replace("{q}", q).replace("None", str(vars))
    else:
        div_cmd = r"\polylongdiv[style=C, div=:, stage={stage}]{{p}}{{q}}"
        div_cmd = (
            div_cmd.replace("{p}", p).replace("{q}", q).replace("{stage}", str(stage))
        )

    s = f"""\\documentclass[border=0.2cm]{{standalone}}
\\usepackage{{polynom}}
\\begin{{document}}
{div_cmd}
\\end{{document}}
    """

    with open("tmp.tex", "w") as f:
        f.write(s)

    os.system("pdflatex tmp.tex")
    if fname.endswith(".svg"):
        fname.strip(".svg")

    if svg:
        os.system(f"pdf2svg tmp.pdf {fname}.svg")
    else:
        os.system(f"mv tmp.pdf {fname}.pdf")

    os.system("rm tmp.*")


if __name__ == "__main__":
    polylongdiv(
        fname="test",
        p="x^3 + 2x^2 - 3x - 6",
        q="x - 2",
        stage=None,
    )
