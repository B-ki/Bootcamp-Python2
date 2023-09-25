from load_image import ft_load
import matplotlib.pyplot as plt
import numpy as np
from pimp_image import ft_invert, ft_red, ft_green, ft_blue, ft_grey


def main():
    img_array = ft_load("../PPGitHubRML.jpg")
    fig, axs = plt.subplots(2, 3)
    axs[0, 0].imshow(img_array)
    axs[0, 0].set_title("Normal")
    invert_img = ft_invert(img_array)
    axs[0, 1].imshow(invert_img)
    axs[0, 1].set_title("Inverted")
    red_img = ft_red(img_array)
    axs[0, 2].imshow(red_img)
    axs[0, 2].set_title("Red")
    green_img = ft_green(img_array)
    axs[1, 0].imshow(green_img)
    axs[1, 0].set_title("Green")
    blue_img = ft_blue(img_array)
    axs[1, 1].imshow(blue_img)
    axs[1, 1].set_title("Blue")
    grey_img = ft_grey(img_array)
    axs[1, 2].imshow(grey_img, cmap=plt.get_cmap('gray'))
    axs[1, 2].set_title("Grey")
    for i, ax in enumerate(axs.flat):
        ax.axis('off')
    plt.tight_layout()
    plt.show()



if __name__ == "__main__":
    main()
