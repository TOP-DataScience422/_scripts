# старшая карта
# (2, 4, 10, 14, 5)
# пара
# (5, 7, 10, 4, 5)
# две пары
# (4, 5, 6, 6, 5)
# сет
# (7, 7, 2, 14, 7)
# фулл-хаус
# (4, 5, 4, 4, 5)
# стрит
# (4, 5, 6, 7, 8)
# каре
# (5, 5, 5, 4, 5)


# переменные для аннотаций
Hand = tuple[int, int, int, int, int]


def poker_combination(hand: Hand) -> str:
    """Находит самую старшую комбинацию в переданной последовательности номиналов карт. Возвращает название комбинации."""
    unique = set(hand)
    unique_len = len(unique)
    
    if unique_len == 4:
        return 'пара'
    
    if unique_len == 3:
        max_repeats = max(hand.count(c) for c in unique)
        if max_repeats == 2:
            return 'две пары'
        else:
            return 'сет'
    
    min_card = min(unique)
    street = list(range(min_card, min_card+5))
    if sorted(hand) == street:
        return 'стрит'
    
    if unique_len == 2:
        max_repeats = max(hand.count(c) for c in unique)
        if max_repeats == 3:
            return 'фулл-хаус'
        else:
            return 'каре'
    
    return 'старшая карта'


from random import randrange as rr

def calc_comb_prob(combination: str, N: int = 100):
    """Находит оценочную частоту выпадения переданной комбинации."""
    results = []
    for _ in range(N):
        cnt = 1
        while True:
            hand = tuple(rr(2, 15) for _ in range(5))
            if poker_combination(hand) != combination:
                cnt += 1
            else:
                break
        results.append(cnt)
        cnt = 1
    return round(sum(results) / len(results))

