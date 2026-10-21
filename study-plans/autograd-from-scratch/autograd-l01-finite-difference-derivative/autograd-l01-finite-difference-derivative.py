import numpy as np

def finite_difference_derivative(coefficients: list, x: float, h: float) -> tuple[float, float, float]:
    """
    Returns the value at x, the value at x plus h, and the estimated slope.
    """

    f = lambda p, coeffs, a, acc=0: 0 if not coeffs else coeffs[0] + a * p(p, coeffs[1:], a)

    f_init = float(f(f, coefficients, x))
    f_h = float(f(f, coefficients, x + h))
    
    return f_init, f_h, (f_h - f_init) / h