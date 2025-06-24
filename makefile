all: macro.h style.css webpconv
	rm -f operewebp/*
	gcc -E -P macro.h -o index.html
	./webpconv opere/*

webpconv: webpconv.c 
	gcc webpconv.c webp/lib/libwebp.a webp/lib/libsharpyuv.a -lm -O2 -Wall -Wextra -o webpconv

