import re
import sys

fname = sys.argv[1]
words = {
    "Example": "Eksempel",
    "Theorem": "Setning",
    "Algorithm": "Algoritme",
    "Proof": "Bevis",
    "Lemma": "Lemma",
    "Corollary": "Korollar",
    "Definition": "Definisjon",
    "Remark": "Merknad",
    "Observation": "Observasjon",
}

html_text = []
with open(fname, "r") as infile:
    lines = infile.readlines()

    for line in lines:
        for key, value in words.items():
            line = re.sub(key, value, line)
        html_text.append(line)


# Write the modified text to the file
with open(fname, "w") as outfile:
    outfile.writelines(html_text)


    

    