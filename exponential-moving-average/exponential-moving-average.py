def exponential_moving_average(values: list, alpha: float) -> list:
    """
    Returns the exponential moving average at every position.
    """

    ema = [values[0]]

    for i, val in enumerate(values[:-1]):
      ema.append(alpha * values[i + 1] + (1.0 - alpha) * ema[i])

    return ema