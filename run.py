from service import Requests
from utils import Shop, Store

print("\nВас приветствует логистическая программа!\n")

while True:
    input_string = input("Введите строку формата \'**Доставить**"
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
        req = Requests(enter_value)
        data = req.departure_destination()
        print(f"Курьер забирает {data['amount']} {data['product']} из {data['from']}")
        if data['from'] == 'магазин':
            Shop.remove(data['product'], data['amount'])
            Store.add(data['product'], data['amount'], )
        else:
            Store.remove(data['product'], data['amount'], )
            Shop.add(data['product'], data['amount'])
        print(f"Курьер везет {enter_value[1]} {enter_value[2]} с {enter_value[4]} в {enter_value[6]}")
        print(f"Курьер доставил {enter_value[1]} {enter_value[2]} в {enter_value[6]}\n")
        print(f"В склад хранится:\n {Store.get_items()}\n")
        print(f"В магазин хранится:\n {Shop.get_items()}\n")

# if __name__ == "__main__":
#     main()