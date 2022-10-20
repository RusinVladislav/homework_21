from abstract_storage import AbstractStorage
from exceptions import BadRequestError, NameStoreError, NameShopError


class Request:
    def __init__(self, request: str, storages: dict[str, AbstractStorage]):
        split_request: list[str] = request.strip().lower().split(' ')
        if len(split_request) != 7:
            raise BadRequestError

        self.amount = int(split_request[1])
        self.product = split_request[2]
        self.departure = split_request[4]
        self.destination = split_request[6]

        if self.departure not in storages:
            raise NameStoreError
        elif self.destination not in storages:
            raise NameShopError
