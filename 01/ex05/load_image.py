import numpy as np
from PIL import Image


def ft_load(path: str) -> np.array:
    assert isinstance(path, str), f"{path} is not a string"
    try:
        img = Image.open(path)
        img_array = np.asarray(img)
        print(f"The shape of the image is: {img_array.shape}")
        return img_array
    except IOError:
        print(f"{path} is not an image")
