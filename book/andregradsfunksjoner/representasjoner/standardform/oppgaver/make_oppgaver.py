import os


def read_file(fname):
    with open(fname) as infile:
        file = infile.readlines()

    return file


def get_admonition_class(fname):
    admonition_class = []
    with open(fname) as infile:
        for i, line in enumerate(infile):
            if i < 3:
                admonition_class.append(line)
            else:
                break

    admonition_class = "".join(admonition_class)
    return admonition_class


def make_problem_set(files):
    with open("oppgaver.md", "w") as outfile:
        outfile.write("# Oppgaver")  # Make header
        outfile.write("\n" * 4)  # Insert new lines for spacing

        # Insert problems
        for i, file in enumerate(files):
            # admonition_class = "".join(read_file(file)[:3])
            admonition_class = get_admonition_class(file)
            delimiter = ":" * 25
            problem_text = f"""
:::{{include}} {file}
:::
"""
            header = f"Oppgave {i + 1}"
            top_delimiter = "".join([delimiter, "{admonition}"])
            header = " ".join([top_delimiter, header])
            content = "\n".join([header, admonition_class, problem_text, delimiter])
            outfile.write(content)

            outfile.write("\n" * 4)
            outfile.write("-" * 3)
            outfile.write("\n" * 4)


BASE_DIR = os.getcwd()


# print(BASE_DIR)
# print(os.listdir(BASE_DIR))
files = []
for dir in os.listdir(path=BASE_DIR):
    if dir.startswith("oppgave_"):
        fname = os.path.join(dir, "oppgave.md")
        if os.path.exists(fname):
            files.append(fname)


files = sorted(files)
print(files)
make_problem_set(files)
