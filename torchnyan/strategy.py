import torch
from hypothesis import strategies as st
from torch.nn import init

TINY_BATCH_SIZE = 5
TINY_TOKEN_SIZE = 11
TINY_FEATURE_DIM = 13

if torch.cuda.is_available():
    BATCH_SIZE = 53
    TOKEN_SIZE = 83
    FEATURE_DIM = 107
else:
    BATCH_SIZE = 37
    TOKEN_SIZE = 53
    FEATURE_DIM = 61

if torch.cuda.is_available():
    device = torch.device('cuda:0')
else:
    device = torch.device('cpu')

tensor = torch.empty((1024, 1024), device=device)
init.orthogonal_(tensor)
del tensor


@st.composite
def sizes(draw, *size: int, min_size: int = 1):
    max_size, *size = size
    n = draw(st.integers(min_value=min_size, max_value=max_size))

    if len(size) == 0:
        return n

    return draw(st.lists(sizes(*size), min_size=n, max_size=n))
