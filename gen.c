#define STB_IMAGE_IMPLEMENTATION
#include "stb_image.h"
#include "webp/encode.h"
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <dirent.h>
#include <unistd.h>
#include <sys/types.h>
#include <sys/stat.h>
#include <errno.h>

#define LENGTH(x) (sizeof(x) / sizeof((x)[0]))
#define STR_BUFF_SIZE 1024
#define QUALITY 70

const char* images[] = {
    "firepunch", "faccia", "rosa", "Puccini", "tauros", "frieren"
};

int remove_regular_files(const char *path) {
    DIR *dir = opendir(path);
    if (dir == NULL) {
        perror("opendir");
        return -1;
    }

    struct dirent *entry;
    char filepath[1024];

    while ((entry = readdir(dir)) != NULL) {
        if (strcmp(entry->d_name, ".") == 0 || strcmp(entry->d_name, "..") == 0)
            continue;

        snprintf(filepath, sizeof(filepath), "%s/%s", path, entry->d_name);

        struct stat st;
        if (stat(filepath, &st) == -1) {
            perror("stat");
            continue;
        }

        if (S_ISREG(st.st_mode)) {
            if (unlink(filepath) == -1) {
                perror("unlink");
            } else {
                printf("Removed: %s\n", filepath);
            }
        }
    }

    closedir(dir);
    return 0;
}

int convert_to_webp(const char *input_file) {
    char name[STR_BUFF_SIZE];
    snprintf(name, STR_BUFF_SIZE, "opere/%s.png", input_file);
    printf("Loading: %s\n", name);

    int width, height, channels;
    unsigned char *image_data = stbi_load(name, &width, &height, &channels, 3); // force RGB
    if (!image_data) {
        fprintf(stderr, "Failed to load image: %s\n", name);
        return -1;
    }

    uint8_t *webp_data = NULL;
    size_t webp_size = WebPEncodeRGB(image_data, width, height, width * 3, QUALITY, &webp_data);
    if (webp_size == 0 || webp_data == NULL) {
        fprintf(stderr, "Failed to encode to WebP: %s\n", name);
        stbi_image_free(image_data);
        return -1;
    }

    char new_name[STR_BUFF_SIZE];
    snprintf(new_name, STR_BUFF_SIZE, "operewebp/%s.webp", input_file);
    FILE *out = fopen(new_name, "wb");
    if (!out) {
        fprintf(stderr, "fopen failed: %s (%s)\n", new_name, strerror(errno));
        WebPFree(webp_data);
        stbi_image_free(image_data);
        return -1;
    }

    fwrite(webp_data, 1, webp_size, out);
    fclose(out);
    printf("Saved: %s (%zu bytes)\n", new_name, webp_size);

    WebPFree(webp_data);
    stbi_image_free(image_data);
    return 0;
}

int main(void) {
    // Ensure output directory exists
    mkdir("operewebp", 0755);

    // Clean output directory
    remove_regular_files("operewebp");

    // Convert each image
    for (size_t i = 0; i < LENGTH(images); i++) {
        convert_to_webp(images[i]);
    }

    // Generate HTML
    FILE *fhtml = fopen("index.html", "w");
    if (!fhtml) {
        perror("fopen html");
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
        perror("fopen css");
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
            "<img src=\"operewebp/%s.webp\" loading=lazy alt=\"%s\"/>\n"
            "<p>%s</p>\n", images[i], images[i], images[i]);
    }

    fprintf(fhtml, "</body>\n</html>\n");
    fclose(fhtml);

    printf("DONE\n");
    return 0;
}

