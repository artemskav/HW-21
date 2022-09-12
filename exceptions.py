class BaseError(Exception):
    message = "Ошибка!"


class NotFreeSpace(BaseError):
    message = "Не хватает места, попробуйте заказать меньше"


class NotFreeForItems(BaseError):
    message = "Количество наименований товаров исчерпано, попробуйте что-то другое"


class NotNecessaryQuantuty(BaseError):
    message = "Не хватает на складе, попробуйте заказать меньше"


class NotThisProduct(BaseError):
    message = "Нет такого товара!"


class NoValidSpace(BaseError):
    message = "Место отправления или доставки указано не правильно."
