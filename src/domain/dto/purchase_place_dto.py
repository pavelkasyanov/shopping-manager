from uuid import UUID


class PurchasePlaceDto:
    def __init__(self,
                 id: UUID,
                 name: str,
                 address: str):
        self.__id = id
        self.__name = name
        self.__address = address

    # getters and setters

    @property
    def id(self) -> UUID:
        return self.__id

    @id.setter
    def id(self, value: UUID) -> None:
        self.__id = value

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, value: str) -> None:
        self.__name = value

    @property
    def address(self) -> str:
        return self.__address

    @address.setter
    def address(self, value: str) -> None:
        self.__address = value
