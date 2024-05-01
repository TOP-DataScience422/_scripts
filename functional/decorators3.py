from time import perf_counter

exp_prefixes = {
    '': 0,
    'м': 3,
    'мк': 6,
    'н': 9,
}

def timer(exp_prefix: str) -> 'function':
    """Генератор декораторов."""
    exp = exp_prefixes.get(exp_prefix, 0)
    def decorator(func_obj: 'function') -> 'function':
        """Функция-декоратор."""
        def wrapper(*args, **kwargs):
            """Функция-обёртка."""
            start = perf_counter()
            result = func_obj(*args, **kwargs)
            end = perf_counter()
            elapsed = (end - start) * 10**exp
            print(f'вызов {func_obj.__name__} занял {elapsed:.{9-exp}f} {exp_prefix}с')
            return result
        return wrapper
    return decorator


def list_to_set(data: list) -> set:
    return set(data)

list_to_set = timer('мк')(list_to_set)


@timer('м')
def list_to_unique_list(data: list) -> list:
    result = []
    for elem in data:
        if elem not in result:
            result.append(elem)
    return result


from random import randrange as rr

N = 10**4

test_data = [rr(-99, 100) for _ in range(N)]

list_to_set(test_data)
list_to_unique_list(test_data)

