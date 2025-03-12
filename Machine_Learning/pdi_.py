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

def gray_bin(img_gray, limiar = 128):
    img_bin = np.zeros_like(img_gray, dtype=np.uint8)
    img_bin[img_gray >= limiar] = 1
    return img_bin

img_path = "C:\\Users\\Fagundez\\workspace\\FEC-2025\\Machine_Learning\\IMG_20241204_142510 (1).jpg"
img = Image.open(img_path)

rgb_image = np.array(img)
img_gray = rgb_gray(rgb_image)
img_binar = gray_bin(img_gray, limiar=128)
#print(img_gray)

img_gray_pillow = Image.fromarray(img_gray)
output_img = "C:\\Users\\Fagundez\\workspace\\FEC-2025\\Machine_Learning\\img_gray.jpg"
img_gray_pillow.save(output_img)
vision_bin_img = img_binar*255
img_binar_pillow = Image.fromarray(vision_bin_img)
output_img_2 = "C:\\Users\\Fagundez\\workspace\\FEC-2025\\Machine_Learning\\img_bin.jpg"
img_binar_pillow.save(output_img_2)
