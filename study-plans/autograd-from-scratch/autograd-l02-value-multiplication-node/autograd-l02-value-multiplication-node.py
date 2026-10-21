def value_multiplication_node(left: dict, right: dict, output_id: str) -> dict:
    """
    Returns the node dictionary with id, data, grad, op, and parents.
    """

    mul = float(left["data"]) * float(right["data"])

    return {
        "id": output_id,
        "data": mul,
        "grad": 0.0,
        "op": "*",
        "parents": [left, right]
    }
