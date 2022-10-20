class BaseError(Exception):
    message = 'Что-то сломалось'


class NotSpaceError(BaseError):
    message = "На складе не хватает места"


class NoProductError(BaseError):
    message = "Запрашиваемого товара нет на складе"


class LowProductError(BaseError):
    message = "Товара меньше чем Вы запрашиваете"


class MoreMaxUniqueItemsError(BaseError):
    message = "Превышено максимальное количество уникальных товаров на складе"


class BadRequestError(BaseError):
    message = "Не верно составлен запрос"


class NameStoreError(BaseError):
    message = "Ошибка в названии склада или введен не существующий склад"


class NameShopError(BaseError):
    message = "Ошибка в названии магазина или введен не существующий магазин"
