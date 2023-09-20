from load_image import ft_load
from PIL import Image
# from scipy.ndimage import zoom


def main():
    img_array = ft_load("../animal.jpeg")
    # zoomed_array = zoom(img_array, 2)
    Image.fromarray(img_array).show()
    # Image.fromarray(zoomed_array).show()

    
if __name__ == "__main__":
    main()
