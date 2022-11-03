from typing import Sequence
from functools import wraps, lru_cache, partial


def trace(func):
    func.level = 0

    @wraps(func)
    def inner(*args, **kwargs):
        arg_str = ", ".join(map(repr, args))
        kwargs_str = ", ".join(map(lambda k, v: f"{k}={v!r}", kwargs.items()))
        func_args = list(filter(bool, (arg_str, kwargs_str)))
        print("__" * func.level + f"-> {func.__name__}({', '.join(func_args)})")
        func.level += 1
        res = func(*args, **kwargs)
        func.level -= 1
        print("__" * func.level + f"<- {func.__name__}({', '.join(func_args)}) == {res}")
        return res
    return inner
