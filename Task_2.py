def function(**kwargs) -> dict:
    result = dict()
    for k, v in kwargs.items():
        try:
            _ = hash(v)
            result[v] = k
        except TypeError:
            result[str(v)] = k

    return result


print(function(first="one", second=2, third=3, fourth="four", fifth=[2, 3]))