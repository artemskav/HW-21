from exceptions import NotFreeSpace, NotFreeForItems, NotNecessaryQuantuty, NotThisProduct, NoValidSpace
from service import Requests
from utils import Shop, Store

print("\nВас приветствует логистическая программа!\n")
shop = Shop()
store = Store()

while True:
    input_string = input("\nВведите строку формата \'**Доставить**"
                         " 3 печеньки **из** склад **в** магазин\' или СТОП/STOP "
                         "для окончания ввода\n").lower()
    enter_value = input_string.split(" ")
    if input_string in ["stop", "стоп"]:
        print("Завершение работы")
        break
    elif len(enter_value) < 7 or enter_value[0] != "доставить" or enter_value[3] != "из" or enter_value[5] != "в":
        print("Запрос не соотверствует шаблону, повторите ввод.")
    else:
        try:
            req = Requests(enter_value)
            data = req.departure_destination()
            if data['from'] == 'магазин':
                if data["product"] in shop.get_items():
                    if store.add(enter_value[2], int(enter_value[1])):
                        shop.remove(enter_value[2], int(enter_value[1]))
                else:
                    raise NotThisProduct
            else:
                if data["product"] in store.get_items():
                    if shop.add(enter_value[2], int(enter_value[1])):
                        store.remove(enter_value[2], int(enter_value[1]))
                else:
                    raise NotThisProduct

            print(f"Курьер забирает {data['amount']} {data['product']} из {data['from']}")
            print(f"Курьер везет {enter_value[1]} {enter_value[2]} с {enter_value[4]} в {enter_value[6]}")
            print(f"Курьер доставил {enter_value[1]} {enter_value[2]} в {enter_value[6]}\n")
            print(f"В склад хранится:")
            for k, v in store.get_items().items():
                print(f"{k}: {v}")
            print(f"\nВ магазин хранится:")
            for k, v in shop.get_items().items():
                print(f"{k}: {v}")
        except (NotFreeSpace, NotFreeForItems, NotNecessaryQuantuty,
                NotThisProduct, NoValidSpace) as error:
            print(error.message)

