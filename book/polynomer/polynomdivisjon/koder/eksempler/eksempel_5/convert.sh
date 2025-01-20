for file in *.svg; do
    magick -density 600 "$file" "${file%.svg}.png"
done