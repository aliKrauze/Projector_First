def type_check(func):
    def wrapper(*args, **kwargs):
        annotations = func.__annotations__

        for arg, expected_type in annotations.items():
            if arg not in kwargs:
                arg_value = args[0]
            else:
                arg_value = kwargs[arg]

            if not isinstance(arg_value, expected_type):
                raise TypeError(f"Argument {arg} must be of type {expected_type}.")

        if annotations['return'] is not None:
            return_value = func(*args, **kwargs)
            if not isinstance(return_value, annotations['return']):
                raise TypeError(f"Return value must be of type {annotations['return']}.")

        return func(*args, **kwargs)

    return wrapper


@type_check
def add(x: int, y: int) -> int:
    return x + y


print(add(1, 2))
