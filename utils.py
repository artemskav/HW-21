from abc import ABC, abstractmethod
from exceptions import NotFreeSpace, NotFreeForItems, NotNecessaryQuantuty, NotThisProduct

class Storage(ABC):

    @abstractmethod
    def add(self, title, quantity):
        pass

    @abstractmethod
    def remove(self, title, quantity):
        pass

    @abstractmethod
    def _get_free_space(self) -> int:
        pass

    @abstractmethod
    def get_items(self):
        pass

    @abstractmethod
    def _get_unique_items_count(self):
        pass

class Store(Storage):
    __items = {"печеньки": 20, "собачки": 20, "коробки": 20, "свинки": 5, "кошечки": 5}
    __capacity = 100

    def add(self, title, quantity: int):
        if self._get_free_space() < quantity:
            raise NotFreeSpace
        elif len(self.__items) == 0:
            self.__items[title] = quantity
            return True
        elif title in self.__items:
            self.__items[title] += quantity
            return True
        elif title not in self.__items:
            self.__items[title] = quantity
            return True

    def remove(self, title, quantity: int):
        if title not in self.__items:
            raise NotThisProduct
        elif self.__items[title] >= quantity:
            self.__items[title] -= quantity
        elif self.__items[title] < quantity:
            raise NotNecessaryQuantuty
        if self.__items[title] == 0:
            self.__items.pop(title)

    def _get_free_space(self):
        amount = 0
        for value in self.__items.values():
            amount += value
        return self.__capacity - amount

    def get_items(self):
        return self.__items

    def _get_unique_items_count(self):
        return len(self.__items)


class Shop(Storage):
    __items = {"свинки": 5, "кошечки": 4, "ленты": 5}
    __capacity = 20

    def add(self, title, quantity: int):
        if self._get_free_space() < quantity:
            raise NotFreeSpace
        elif len(self.__items) == 0:
            self.__items[title] = quantity
            return True
        elif title in self.__items:
            self.__items[title] += quantity
            return True
        elif self._get_unique_items_count() == 5:
            raise NotFreeForItems
        elif title not in self.__items:
            self.__items[title] = quantity
            return True
        elif self._get_unique_items_count() < 5:
            for item in self.__items:
                if item == title:
                    item.value += quantity
            return True

    def remove(self, title, quantity: int):
        if title not in self.__items:
            raise NotThisProduct
        elif self.__items[title] >= quantity:
            self.__items[title] -= quantity
        elif self.__items[title] < quantity:
            raise NotNecessaryQuantuty
        if self.__items[title] == 0:
            self.__items.pop(title)

    def _get_free_space(self):
        amount = 0
        for value in self.__items.values():
            amount += value
        return self.__capacity - amount

    def get_items(self):
        return self.__items

    def _get_unique_items_count(self):
        return len(self.__items)
