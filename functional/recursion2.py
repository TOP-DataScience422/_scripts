def gcd(num1: int, num2: int) -> int:
    """Рекурсивно находит и возвращает наибольший общий делитель (НОД)."""
    if num2:
        return gcd(num2, num1 % num2)
    else:
        return num1


# breakpoint()
var = gcd(193, 3)

