from datetime import datetime
from uuid import UUID


class PurchaseDto:
    def __init__(self,
                 id: UUID,
                 user_id: UUID,
                 date: datetime,
                 cashbox_number: int,
                 cashier_name: str,
                 total_amount: float,
                 discount_amount: float):
        self.__id = id
        self.__user_id = user_id

        self.__date = date
        self.__cashbox_number = cashbox_number
        self.__cashier_name = cashier_name

        self.__total_amount = total_amount
        self.__discount_amount = discount_amount

    #getters and setters

    @property
    def id(self) -> UUID:
        return self.__id

    @id.setter
    def id(self, value: UUID) -> None:
        self.__id = value

    @property
    def user_id(self) -> UUID:
        return self.__user_id

    @user_id.setter
    def user_id(self, value: UUID) -> None:
        self.__user_id = value

    @property
    def date(self) -> datetime:
        return self.__date

    @date.setter
    def date(self, value: datetime) -> None:
        self.__date = value

    @property
    def cashbox_number(self) -> int:
        return self.__cashbox_number

    @cashbox_number.setter
    def cashbox_number(self, value: int) -> None:
        self.__cashbox_number = value

    @property
    def cashier_name(self) -> str:
        return self.__cashier_name

    @cashier_name.setter
    def cashier_name(self, value: str) -> None:
        self.__cashier_name = value

    @property
    def total_amount(self) -> float:
        return self.__total_amount

    @total_amount.setter
    def total_amount(self, value: float) -> None:
        self.__total_amount = value

    @property
    def discount_amount(self) -> float:
        return self.__discount_amount

    @discount_amount.setter
    def discount_amount(self, value: float) -> None:
        self.__discount_amount = value
