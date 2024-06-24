from numpy import loadtxt, dot
from pathlib import Path
from sys import path


script_dir = Path(path[0])

prices = loadtxt(script_dir / 'prices.data')
amounts = loadtxt(script_dir / 'amounts.data', dtype=int)

totals_by_stores = prices * amounts
total = dot(prices, amounts)

print(
    '\n'.join(f'магазин {i}: {val:,.2f} ₽' 
        for i, val in enumerate(totals_by_stores, 1)
    ),
    f'\nитого: {total:,.2f} ₽'
)

