import numpy as np


def mse_loss(input: np.ndarray, target: np.ndarray, reduction: str = "mean") -> float | np.ndarray:
    """
    input:     shape matching target, any shape
    target:    shape matching input, any shape
    reduction: 'mean' | 'sum' | 'none'

    Returns:
        a Python float when reduction is 'mean' or 'sum';
        an array shaped like input when reduction is 'none'
    """
    # TODO: Implement mean squared error from Theory.
    # Branch on `reduction` explicitly. Raise ValueError for anything else.

    diff = input - target
    if reduction == "mean":
        return float(np.mean(diff ** 2))
    elif reduction == "sum":
        return float(np.sum(diff ** 2))
    elif reduction == "none":
        return diff ** 2
    else:
        raise ValueError(f"Invalid reduction: {reduction!r}. Must be 'mean', 'sum', or 'none'.")
    pass
