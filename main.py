import app as app

from exceptions import NotFreeSpace, NotFreeForItems, NotNecessaryQuantuty, NotThisProduct, NoValidSpace
from service import Requests
from utils import Shop, Store

print("\nВас приветствует логистическая программа!\n")
sim = True
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
        continue
    else:
        try:
            req = Requests(enter_value)
            data = req.departure_destination()
            if data['from'] == 'магазин':
                store.add(enter_value[2], int(enter_value[1]))
#                global sim
                if sim:
                    shop.remove(enter_value[2], int(enter_value[1]))
            else:
                shop.add(enter_value[2], int(enter_value[1]))
#                global sim
                if sim:
                    store.remove(enter_value[2], int(enter_value[1]))
            print(f"Курьер забирает {data['amount']} {data['product']} из {data['from']}")
            print(f"Курьер везет {enter_value[1]} {enter_value[2]} с {enter_value[4]} в {enter_value[6]}")
            print(f"Курьер доставил {enter_value[1]} {enter_value[2]} в {enter_value[6]}\n")
            print(f"В склад хранится:")
            for k, v in store.get_items().items():
                print(f"{k}: {v}")
            print(f"\nВ магазин хранится:")
            for k, v in shop.get_items().items():
                print(f"{k}: {v}")
        except NotFreeSpace as error:
            print(error.message)
        except NotFreeForItems as error:
            print(error.message)
        except NotNecessaryQuantuty as error:
            print(error.message)
        except NotThisProduct as error:
            print(error.message)
        except NoValidSpace as error:
            print(error.message)
        continue
#
# if __name__ == "__main__":
#     app.run(debug=True)