from uuid import UUID


class ProductDto:
    def __init__(self,
                 id: UUID,
                 purchase_id: UUID,
                 type_id: UUID,
                 subtype_id: UUID,
                 count: float,
                 unit_price: float,
                 unit_price_with_discount: float,
                 remark: str):
        self.__id = id
        self.__purchase_id = purchase_id
        self.__type_id = type_id
        self.__subtype_id = subtype_id
        self.__count = count
        self.__unit_price = unit_price
        self.__remark = remark
        self.__unit_price_with_discount = unit_price_with_discount

    # getters and setters

    @property
    def id(self) -> UUID:
        return self.__id

    @id.setter
    def id(self, value: UUID) -> None:
        self.__id = value

    @property
    def purchase_id(self) -> UUID:
        return self.__purchase_id

    @purchase_id.setter
    def purchase_id(self, value: UUID) -> None:
        self.__purchase_id = value

    @property
    def type_id(self) -> UUID:
        return self.__type_id

    @type_id.setter
    def type_id(self, value: UUID) -> None:
        self.__type_id = value

    @property
    def subtype_id(self) -> UUID:
        return self.__subtype_id

    @subtype_id.setter
    def subtype_id(self, value: UUID) -> None:
        self.__subtype_id = value

    @property
    def count(self) -> float:
        return self.__count

    @count.setter
    def count(self, value: float) -> None:
        self.__count = value

    @property
    def unit_price(self) -> float:
        return self.__unit_price

    @unit_price.setter
    def unit_price(self, value: float) -> None:
        self.__unit_price = value

    @property
    def remark(self) -> str:
        return self.__remark

    @remark.setter
    def remark(self, value: str) -> None:
        self.__remark = value

    @property
    def unit_price_with_discount(self) -> float:
        return self.__unit_price_with_discount

    @unit_price_with_discount.setter
    def unit_price_with_discount(self, value: float) -> None:
        self.__unit_price_with_discount = value
