def check_if_types_match(type: str, arr: list[int]):
    types_map = {
                "int": int,
                "float": float
                }
    return all(isinstance(x, types_map[type]) for x in arr)