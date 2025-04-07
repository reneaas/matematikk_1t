build:
	PYTHONPATH=$PYTHONPATH:$(pwd) python3 update_quiz_figures.py
	PYTHONPATH=$PYTHONPATH:$(pwd) jb build .

full:
	export PYTHONPATH=$PYTHONPATH:$(pwd) python3 update_quiz_figures.py
	PYTHONPATH=$PYTHONPATH:$(pwd) jb build . --all

pdfs:
	zsh build_individual_pdfs.sh