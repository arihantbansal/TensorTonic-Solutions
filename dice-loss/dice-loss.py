import numpy as np

def dice_loss(p: list, y: list, eps: float = 1e-8) -> float:
    """
    Returns the loss as a float.
    """
    
    p = np.asarray(p, dtype=float)
    y = np.asarray(y, dtype=float)

    dice = (2 * np.sum(p * y).item() + eps) / (np.sum(p).item() + np.sum(y).item() + eps)

    loss = 1 - dice

    return loss
    