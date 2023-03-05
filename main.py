import matplotlib.pyplot as plt
import numpy as np

from quilting import *
from texture_transfer import *


texture_1 = plt.imread('C:\\Users\\adria\\Documents\\Mestrado\\image_quilting_adriano\\data\\texture1.jpg').astype(np.float32)

block_size = 100
overlap_size = int(block_size / 6)


show_fig2c(synth_texture(texture_1, block_size, overlap_size))

source_texture = plt.imread('data/texture6.jpg').astype(np.float32)
target_image = plt.imread('data/bill.jpg').astype(np.float32)

block_size = 30
overlap_size = int(block_size / 6)

def show_text_trans(img):
    plt.title('Texture Transfer')
    plt.imshow(normalize_img(img))
    plt.axis('off')
    plt.show()

show_text_trans(transfer_texture(source_texture, target_image, block_size, overlap_size))

