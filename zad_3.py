
class Property:
    def __init__(
            self, area: int, rooms: int, price: int, address: str
    ) -> None:
        self.area = area
        self.rooms = rooms
        self.price = price
        self.address = address

    def __str__(self) -> str:
        return f'Area: {self.area},' \
               f' rooms: {self.rooms}, ' \
               f'price: {self.price}, ' \
               f'address: {self.address}'


class House(Property):
    def __init__(
            self, area: int, rooms: int, price: int, address: str, plot: int
    ) -> None:
        super().__init__(area, rooms, price, address)
        self.plot = plot

    def __str__(self) -> str:
        return f'Area: {self.area}, ' \
               f'rooms: {self.rooms}, ' \
               f'price: {self.price}, ' \
               f'address: {self.address}, ' \
               f'plot size: {self.plot}'


class Flat(Property):
    def __init__(
            self, area: int, rooms: int, price: int, address: str, floor: int
    ) -> None:
        super().__init__(area, rooms, price, address)
        self.floor = floor

    def __str__(self) -> str:
        return f'Area: {self.area}, ' \
               f'rooms: {self.rooms}, ' \
               f'price: {self.price}, ' \
               f'address: {self.address}, ' \
               f'floor: {self.floor}'


my_house = House(100, 4, 800000, "Tichau", 1100)
print(my_house.__str__())
my_flat = Flat(100, 3, 5000000, "Gleiwitz", 2)
print(my_flat.__str__())
