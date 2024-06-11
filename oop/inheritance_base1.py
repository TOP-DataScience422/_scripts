from datetime import date, datetime as dt, timedelta as td


class Product:
    date_format: str = '%d.%m.%Y'
    
    def __init__(
            self, 
            name: str, 
            days_to_expire: int,
            produced: date | str = date.today(),
    ):
        self.name = name
        if isinstance(produced, str):
            produced = dt.strptime(produced, self.date_format).date()
        self.produced: date = produced
        self.expired: date = produced + td(days=days_to_expire)
    
    def is_expired(self) -> bool:
        return date.today() > self.expired
    
    def __repr__(self):
        return f'<{self.name}: {self.produced:{self.date_format}}—{self.expired:{self.date_format}}>'


class Fridge(list):
    def __repr__(self):
        products = '\n'.join(repr(pr) for pr in self)
        return '\n'.join((
            'ХОЛОДИЛЬНИК',
            '-----------',
            products
        ))
    
    def append(self, product: Product):
        if isinstance(product, Product):
            super().append(product)
        else:
            raise TypeError(f"{self.__class__.__name__!r} can contain only 'Product' instances")
    
    def clear_expired(self) -> None:
        for pr in [pr for pr in self if pr.is_expired()]:
            self.remove(pr)


products = (
    Product('молоко', 7, '27.05.2024'),
    Product('морковь', 15, '20.04.2024'),
    Product('хлеб ржаной', 5, date.today()),
    Product('шоколад', 120, '8.03.2024'),
)
minsk = Fridge(products)

# >>> minsk
# ХОЛОДИЛЬНИК
# -----------
# <молоко: 27.05.2024—03.06.2024>
# <морковь: 20.04.2024—05.05.2024>
# <хлеб ржаной: 01.06.2024—06.06.2024>
# <шоколад: 08.03.2024—06.07.2024>
# >>>
# >>> minsk.clear_expired()
# >>> minsk
# ХОЛОДИЛЬНИК
# -----------
# <молоко: 27.05.2024—03.06.2024>
# <хлеб ржаной: 01.06.2024—06.06.2024>
# <шоколад: 08.03.2024—06.07.2024>
