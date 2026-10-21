def scalar_expression_partials(a: float, b: float, c: float, h: float) -> tuple[float, float, float, float]:
    """
    Returns the expression value and numerical partials for a, b, and c.
    """

    d = lambda a, b, c: a * b + c

    d_init = float(d(a, b, c))

    da = (d(a + h, b, c) - d_init) / h
    db = (d(a, b + h, c) - d_init) / h
    dc = (d(a, b, c + h) - d_init) / h
    
    
    return d_init, da, db, dc