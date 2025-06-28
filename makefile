all: style.css gen.c
	@gcc gen.c webp/lib/libwebp.a webp/lib/libsharpyuv.a -lm -O2 -Wall -Wextra -o gen
	@./gen


