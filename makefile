build:
	PYTHONPATH=$PYTHONPATH:$(pwd) jb build .

all:
	PYTHONPATH=$PYTHONPATH:$(pwd) jb build . --all

clean:
	rm -r ./_static/figurer
	rm -r ./_static/polydiv
	rm -r ./_static/horner

