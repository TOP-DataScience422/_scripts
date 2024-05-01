def catcher(func_obj: 'function') -> 'function':
    def wrapper(*args, **kwargs):
        try:
            result = func_obj(*args, **kwargs)
        except Exception as exc:
            print(f'{exc.__class__.__name__}: {exc}')
        else:
            return result
    return wrapper


@catcher
def divider(num1, num2) -> float:
    return num1 / num2


# >>> divider(1, 5)
# 0.2
# >>> divider(1, 25)
# 0.04
# >>> divider(1, 0)
# ZeroDivisionError: division by zero
# >>>

