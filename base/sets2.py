one_digit = set(range(1, 10))
naturals_before_10 = set(range(1, 10))
naturals_before_20 = set(range(1, 20))

# >>> one_digit
# {1, 2, 3, 4, 5, 6, 7, 8, 9}
# >>>
# >>> before_20
# {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19}
# >>>
# >>> naturals_before_10
# {1, 2, 3, 4, 5, 6, 7, 8, 9}

# >>> one_digit == naturals_before_10
# True
# >>>
# >>> one_digit < naturals_before_10
# False
# >>> one_digit <= naturals_before_10
# True
# >>>
# >>> one_digit < before_20
# True
# >>> one_digit <= before_20
# True
# >>> before_20 > one_digit
# True
