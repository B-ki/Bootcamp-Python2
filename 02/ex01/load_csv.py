import pandas as pd
import os


def load(path: str) -> pd.DataFrame:
    assert os.path.exists(path), f"The file {path} does not exists"
    ret = pd.read_csv(path)
    print(f"Loading dataset of dimensions {ret.shape}")
    return ret
