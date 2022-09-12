from exceptions import NoValidSpace

class Requests:

    def __init__(self, input_string: list):
        self._from = input_string[4]
        self._to = input_string[6]
        self._amount = int(input_string[1])
        self._product = input_string[2]

    def departure_destination(self):
        if self._from == "склад" and self._to == "магазин":
            return {"from": "склад", "to": "магазин", "amount": self._amount, "product": self._product}
        elif self._from == "магазин" and self._to == "склад":
            return {"from": "магазин", "to": "склад", "amount": self._amount, "product": self._product}
        else:
            raise NoValidSpace
