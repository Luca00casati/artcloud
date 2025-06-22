all: macro.h style.css
	gcc -E -P macro.h -o index.html

