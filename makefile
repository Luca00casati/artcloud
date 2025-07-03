all: style.css gen.c
	@gcc gen.c -Wall -Wextra -o gen
	@./gen

