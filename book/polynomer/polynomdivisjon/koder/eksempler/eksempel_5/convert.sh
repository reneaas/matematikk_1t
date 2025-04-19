for file in *.svg; do
    magick -background none -density 600 "$file" "${file%.svg}.png"
done