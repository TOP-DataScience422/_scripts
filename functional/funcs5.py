def track_detail(
        *,
        title,
        artist,
        album,
        channels,
        bit_depth,
        sample_rate
):
    ...
    print(
        f'{title=}',
        f'{artist=}',
        f'{album=}',
        f'{channels=}',
        f'{bit_depth=}',
        f'{sample_rate=}',
        sep='\n'
    )
    ...


# >>> track_detail(
# ...     'Boom',
# ...     'Boomers',
# ...     'BOOM!',
# ...     6,
# ...     8,
# ...     96000
# ... )
# TypeError: track_detail() takes 0 positional arguments but 6 were given
# >>>
# >>> track_detail(
# ...     title='Boom',
# ...     artist='Boomers',
# ...     album='BOOM!',
# ...     channels=6,
# ...     bit_depth=8,
# ...     sample_rate=96000
# ... )
# title='Boom'
# artist='Boomers'
# album='BOOM!'
# channels=6
# bit_depth=8
# sample_rate=96000


def func(pos, /, pos_key, *, key1, key2=False):
    ...

