from uuid import UUID


class ProductSubTypeDto:
    def __init__(self,
                 id: UUID,
                 name: str,
                 product_type_id: UUID):
        self.__id = id
        self.__name = name
        self.__product_type_id = product_type_id

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
    def product_type_id(self) -> UUID:
        return self.__product_type_id

    @product_type_id.setter
    def product_type_id(self, value: UUID) -> None:
        self.__product_type_id = value
