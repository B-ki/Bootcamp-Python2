from load_image import ft_load
import matplotlib.pyplot as plt
import numpy as np


def main():
    img_array = ft_load("../animal.jpeg")
    red_image = img_array[:, :, 0]
    new_array = red_image[100:500, 450:850]
    new_array = np.rot90(new_array)
    fig, ax = plt.subplots()
    ax.imshow(new_array, cmap='gray')
    plt.show()


if __name__ == "__main__":
    main()
