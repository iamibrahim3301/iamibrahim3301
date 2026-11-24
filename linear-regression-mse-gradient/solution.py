import numpy as np


def mse_gradient(
    input: np.ndarray,
    weight: np.ndarray,
    bias: np.ndarray | None,
    target: np.ndarray,
) -> tuple[np.ndarray, np.ndarray | None]:
    """
    input:  shape (batch_size, in_features)
    weight: shape (out_features, in_features)
    bias:   shape (out_features,), or None
    target: shape (batch_size, out_features)

    Returns:
        grad_weight: same shape as weight
        grad_bias: same shape as bias, or None if bias is None
    """
    # TODO: Implement the gradient formulas derived in Theory.
    # Do not use an autograd library -- these are the manual derivatives.
    pred = input @ weight.T
    if bias is not None:
        pred = pred + bias

    grad_pred = (2.0 / pred.size) * (pred - target)

    grad_weight = grad_pred.T @ input
    grad_bias = np.sum(grad_pred, axis=0) if bias is not None else None

    return grad_weight, grad_bias
    pass
