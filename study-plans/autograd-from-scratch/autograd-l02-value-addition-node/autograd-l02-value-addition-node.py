def value_addition_node(left: dict, right: dict, output_id: str) -> dict:
    """
    Returns an addition node with id, data, grad, op, and the original parents.
    """

    sum = float(left["data"]) + float(right["data"])

    return {
        "id": output_id,
        "data": sum,
        "grad": 0.0,
        "op": "+",
        "parents": [left, right]
    }