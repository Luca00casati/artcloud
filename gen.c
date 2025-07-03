#include <stdio.h>
#include <string.h>
#include <stdlib.h>

#define LENGTH(x) (sizeof(x) / sizeof((x)[0]))

const char* images[] = {
    "firepunch", "faccia", "rosa", "Puccini", "tauros", "frieren", "viola"
};

// Comparison function for qsort
int qsortstrcmp(const void *a, const void *b) {
    return strcmp(*(const char **)a, *(const char **)b);
}

int main(void) {
    //sortimages
    qsort(images, LENGTH(images), sizeof(char *), qsortstrcmp);

    // Generate HTML
    FILE *fhtml = fopen("index.html", "w");
    if (!fhtml) {
        fprintf(stderr,"error open html\n");
        return 1;
    }

    fprintf(fhtml,
        "<!doctype html>\n"
        "<html lang=it>\n"
        "<head>\n"
        "<meta charset=UTF-8 />\n"
        "<meta name=viewport content=width=device-width, initial-scale=1.0 />\n"
        "<link rel=icon href=siteres/icon/favicon.svg type=image/svg+xml />\n"
        "<title>La mia galleria</title>\n");

    FILE *fcss = fopen("style.css", "r");
    if (!fcss) {
        fprintf(stderr,"error open css\n");
        fclose(fhtml);
        return 1;
    }

    int ch;
    while ((ch = fgetc(fcss)) != EOF) {
        fputc(ch, fhtml);
    }
    fclose(fcss);

    fprintf(fhtml, "</head>\n<body>\n");

    for (size_t i = 0; i < LENGTH(images); i++) {
        fprintf(fhtml,
            "<img src=\"opere/%s.png\" loading=lazy alt=\"%s\"/>\n"
            "<p>%s</p>\n", images[i], images[i], images[i]);
    }

    fprintf(fhtml, "</body>\n</html>\n");
    fclose(fhtml);

    printf("DONE\n");
    return 0;
}

