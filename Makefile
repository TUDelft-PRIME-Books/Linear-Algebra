new:
	jupyter-book build  . 
config:
	jupyter-book config sphinx .
all : config
	jupyter-book build --all . 
