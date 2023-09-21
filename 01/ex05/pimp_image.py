import numpy as np


def ft_invert(array) -> np.ndarray:
    assert isinstance(array, np.ndarray), "array is not a numpy array"
    return 255 - array[:, :, :3]


def ft_red(array) -> np.ndarray:
    assert isinstance(array, np.ndarray), "array is not a numpy array"
    copy = array[:, :, :3].copy()
    copy[:, :, (1, 2)] = 0
    return copy


def ft_green(array) -> np.ndarray:
    assert isinstance(array, np.ndarray), "array is not a numpy array"
    copy = array[:, :, :3].copy()
    copy[:, :, (0, 2)] = 0
    return copy


def ft_blue(array) -> np.ndarray:
    assert isinstance(array, np.ndarray), "array is not a numpy array"
    copy = array[:, :, :3].copy()
    copy[:, :, (0, 1)] = 0
    return copy


def ft_grey(array) -> np.ndarray:
    assert isinstance(array, np.ndarray), "array is not a numpy array"
    return np.dot(array[...,:3], [0.2989, 0.5870, 0.1140])
