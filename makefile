build:
	rm -r ./_static/figurer
	PYTHONPATH=$PYTHONPATH:$(pwd) jb build .

all:
	rm -r ./_static/figurer
	PYTHONPATH=$PYTHONPATH:$(pwd) jb build . --all

clean:
	rm -r ./_static/figurer

