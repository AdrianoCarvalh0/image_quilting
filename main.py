import matplotlib.pyplot as plt
import numpy as np

from quilting import * 

texture_1 = plt.imread('C:\\Users\\adria\\Documents\\Mestrado\\image_quilting_adriano\\data\\texture1.jpg').astype(np.float32)

block_size = 100
overlap_size = int(block_size / 6)

show_fig2c(synth_texture(texture_1, block_size, overlap_size))

