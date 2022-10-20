from exceptions import MoreMaxUniqueItemsError
from store import Store


class Shop(Store):
    def __init__(self, items: dict[str, int], capacity: int, max_unique_items: int):
        super().__init__(items, capacity)
        self.max_unique_items = max_unique_items

    def add(self, name: str, quantity: int) -> None:
        if self.get_unique_items_count() >= self.max_unique_items:
            raise MoreMaxUniqueItemsError

        super().add(name, quantity)
