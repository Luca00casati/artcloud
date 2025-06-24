#include <stdio.h>
#include <string.h>
int main(int argc, const char *argv[]){
    for (int i = 1; i < argc; i++) {
    printf("%s\n", argv[i]);
    printf("%zu\n", strlen(argv[i]));
    const char * index = argv[i];
    size_t original_len = strlen(index);
    char name[original_len - 10 + 1];
    for (int j = 0, i = 6; i < original_len - 4; i++, j++){
        name[j] = index[i];
    }
    name[original_len - 10] = '\0';
    printf("%s\n", name);
    size_t new_len = 15 + original_len - 10;
    char new_name[15 + original_len - 10 + 1]; 
    snprintf(new_name, 15 + original_len - 10 + 1, "operejpeg/%s.jpeg", name);
    printf("%s\n", new_name);

     int width, height, channels;
    unsigned char *image_data = stbi_load(index, &width, &height, &channels, 3); // force RGB
    if (!image_data) {
        fprintf(stderr, "Failed to load image: %s\n", input_file);
        return 1;
    }

    uint8_t *webp_data = NULL;
    size_t webp_size = WebPEncodeRGB(image_data, width, height, width * 3, 70, &webp_data);
    if (webp_size == 0) {
        fprintf(stderr, "Failed to encode to WebP\n");
        stbi_image_free(image_data);
        return 1;
    }

    FILE *out = fopen(new_name, "wb");
    if (!out) {
        perror("fopen");
        WebPFree(webp_data);
        stbi_image_free(image_data);
        return 1;
    }

    fwrite(webp_data, 1, webp_size, out);
    fclose(out);

    printf("Saved: %s (%zu bytes)\n", new_name, webp_size);

    WebPFree(webp_data);
    stbi_image_free(image_data);
    }
    return 0;
}
