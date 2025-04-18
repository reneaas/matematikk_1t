build:
	python update_quiz_figures.py
	PYTHONPATH=$PYTHONPATH:$(pwd) jb build .

all:
	python update_quiz_figures.py
	PYTHONPATH=$PYTHONPATH:$(pwd) jb build . --all

clean:
	rm -r ./_static/figurer

