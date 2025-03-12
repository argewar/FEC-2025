from PIL import Image
import numpy as np

def rgb_gray(rgb_image):
    altura, largura, canais = rgb_image.shape
    gray_image = np.zeros((altura, largura), dtype=np.uint8)

    for i in range(altura):
        for j in range(largura):
            r = rgb_image[i, j, 0]
            g = rgb_image[i, j, 1]
            b = rgb_image[i, j, 2]

            gray = 0.2989 * r + 0.5870 * g + 0.1140 * b

            gray = max(0, min(gray, 255))

            gray_image[i, j] = int(gray)
            
    return gray_image

img_path = "C:\\Users\\Fagundez\\workspace\\FEC-2025\\Machine_Learning\\IMG_20241204_142510 (1).jpg"
img = Image.open(img_path)

rgb_image = np.array(img)
img_gray = rgb_gray(rgb_image)

print(img_gray)
