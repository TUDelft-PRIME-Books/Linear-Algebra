current: all

new:
	jupyter-book build  . 
all : 
	jupyter-book build --all . 
pdf:
	jupyter-book build --builder pdflatex --path-output ${HOME}/test/jpbooks .
