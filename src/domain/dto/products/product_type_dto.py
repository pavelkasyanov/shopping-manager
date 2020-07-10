from uuid import UUID


class ProductTypeDto:
    def __init__(self,
                 id: UUID,
                 name: str):
        self.__id = id
        self.__name = name

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

