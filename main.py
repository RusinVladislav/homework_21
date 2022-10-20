from abstract_storage import AbstractStorage
from exceptions import BaseError
from request import Request
from shop import Shop
from store import Store
from transport import Transport

store = Store(
    items={
        'мясо': 5,
        'молоко': 10,
        'носки': 50,
    },
    capacity=100,
)

shop = Shop(
    items={
        'мясо': 1,
        'молоко': 3,
    },
    capacity=20,
    max_unique_items=5,
)

storages: dict[str, AbstractStorage] = {
    'склад': store,
    'магазин': shop,
}


def main():
    print("Здравствуйте!\n")

    while True:
        # Выводим содержимое складов.
        for storage_name, storage in storages.items():
            print(f"В {storage_name} хранится: {storage.get_items()}")

        # Запрашиваем у пользователя request.
        user_request: str = input(
            "\nВведите запрос в формате: 'Доставить 3 молоко из склад в магазин'\n"
            "Введите 'стоп' или 'stop' что бы завершить работу\n"
        )

        if user_request in ('stop', 'стоп'):
            break

        # Обрабатываем запрос (строку): проверяем на ошибки, определяем: товар, количество, откуда и куда отправляем.
        try:
            request = Request(request=user_request, storages=storages)
        except BaseError as error:
            print(error.message)

        # Осуществляем доставку товара и выводим соответствующие сообщения
        try:
            item_transport = Transport(request=request, storages=storages)
            item_transport.move()
        except BaseError as error:
            print(error.message)


if __name__ == '__main__':
    main()
