#define STB_IMAGE_IMPLEMENTATION
#include "stb_image.h"

#include "webp/include/encode.h"
#include <stdio.h>
#include <string.h>
#include <pthread.h>

#define MAX_THREADS 8

typedef struct {
    const char *input_file;
} Task;

#define QUALITY 70
void *convert_to_webp(void *arg) {
    Task *task = (Task *)arg;
    const char *index = task->input_file;
    size_t original_len = strlen(index);
    char name[original_len - 10 + 1];
    for (int j = 0, i = 6; i < original_len - 4; i++, j++){
        name[j] = index[i];
    }
    name[original_len - 10] = '\0';
    // printf("%s\n", name);
    size_t new_len = 15 + original_len - 10;
    char new_name[15 + original_len - 10 + 1]; 
    snprintf(new_name, 15 + original_len - 10 + 1, "operejpeg/%s.jpeg", name);
    // printf("%s\n", new_name);

     int width, height, channels;
    unsigned char *image_data = stbi_load(index, &width, &height, &channels, 3); // force RGB
    if (!image_data) {
        fprintf(stderr, "Failed to load image: %s\n", index);
        pthread_exit(NULL);
    }


    uint8_t *webp_data = NULL;
    size_t webp_size = WebPEncodeRGB(image_data, width, height, width * 3, QUALITY, &webp_data);
    if (webp_size == 0) {
        fprintf(stderr, "Failed to encode to WebP\n");
        stbi_image_free(image_data);
        pthread_exit(NULL);
    }

    FILE *out = fopen(new_name, "wb");
    if (!out) {
        perror("fopen");
        WebPFree(webp_data);
        stbi_image_free(image_data);
        pthread_exit(NULL);
    }

    fwrite(webp_data, 1, webp_size, out);
    fclose(out);

    printf("Saved: %s (%zu bytes)\n", new_name, webp_size);

    WebPFree(webp_data);
    stbi_image_free(image_data);
    pthread_exit(NULL);
    }
int main(int argc, char *argv[]) {
    pthread_t threads[MAX_THREADS];
    Task tasks[MAX_THREADS];
    int thread_count = 0;

    for (int i = 1; i < argc; i++) {
        tasks[thread_count].input_file = argv[i];
        pthread_create(&threads[thread_count], NULL, convert_to_webp, &tasks[thread_count]);
        thread_count++;

        // If thread limit reached, wait for all to finish before continuing
        if (thread_count == MAX_THREADS || i == argc - 1) {
            for (int t = 0; t < thread_count; t++) {
                pthread_join(threads[t], NULL);
            }
            thread_count = 0;
        }
    }
    return 0;
}
