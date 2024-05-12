UserId = int
ProductId = str
ProductTypeId = str
ProductSubTypeId = str


class NotFoundError(Exception):
    ...


class VerificationFailError(Exception):
    ...
