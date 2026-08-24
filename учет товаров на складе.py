warehouse = {
    "laptop": {"price": 80000, "quantity": 5},
    "mouse": {"price": 1500, "quantity": 20},
    "keyboard": {"price": 4000, "quantity": 10}
}

while True:
    print(f"\n")
    print(f"1 - Показать товары. ")
    print(f"2 - Добавить товары. ")
    print(f"3 - Продать товар. ")
    print(f"4 - Пополнить остаток. ")
    print(f"5 - Изменить цену. ")
    print(f"6 - Общая стоимость склада. ")
    print(f"7 - Самый дорогой товар. ")
    print(f"8 - Товары с остатком меньше 3. ")
    print(f"0 - Выход. ")

    choice = input("Выберите действие: ")

    # 1 - Показать товары
    if choice == "1":

        for name, products in warehouse.items():
            print(f"Товар: {name} цена: {products['price']} руб., Остаток {products['quantity']} шт.")

    # 2 - Добавить товар
    elif choice == "2":
        name = input("Введите название товара: ")
        if name in warehouse:
            print(f"Товар {name} уже есть на складе!")
        else:
            price = float(input("Введите цену товара: "))
            quantity = int(input("Введите количество: "))
            warehouse[name] = {"price": price, "quantity": quantity}
            print(f"Товар {name} добавлен!")

    # 3 - Продать товар
    elif choice == "3":
        name = input("Введите название товара для продажи: ")
        if name in warehouse:
            quantity = int(input(f"Сколько продать? (остаток: {warehouse[name]['quantity']}): "))
            if quantity <= warehouse[name]['quantity']:
                warehouse[name]['quantity'] -= quantity
                print(f"Продано {quantity} шт. товара {name}")
                if warehouse[name]['quantity'] == 0:
                    print(f"Товар {name} закончился!")
            else:
                print(f"Недостаточно товара! Остаток: {warehouse[name]['quantity']} шт.")
        else:
            print(f"Товар {name} не найден!")

    # 4 - Пополнить остаток
    elif choice == "4":
        name = input("Введите название товара для пополнения: ")
        if name in warehouse:
            quantity = int(input(f"Сколько добавить? (текущий остаток: {warehouse[name]['quantity']}): "))
            warehouse[name]['quantity'] += quantity
            print(f"Остаток пополнен! Теперь: {warehouse[name]['quantity']} шт.")
        else:
            print(f"Товар {name} не найден!")

    # 5 - Изменить цену
    elif choice == "5":
        name = input("Введите название товара для изменения цены: ")
        if name in warehouse:
            new_price = float(input(f"Введите новую цену (текущая: {warehouse[name]['price']} руб.): "))
            warehouse[name]['price'] = new_price
            print(f"Цена товара {name} изменена на {new_price} руб.")
        else:
            print(f"Товар {name} не найден!")

    # 6 - Общая стоимость склада
    elif choice == "6":
        total = 0
        for products in warehouse.values():
            total += products['price'] * products['quantity']
        print(f"Общая стоимость склада: {total} руб.")

    # 7 - Самый дорогой товар
    elif choice == "7":
        max_price = 0
        expensive_product = ""
        for name, products in warehouse.items():
            if products['price'] > max_price:
                max_price = products['price']
                expensive_product = name
        print(f"Самый дорогой товар: {expensive_product} - {max_price} руб.")

    # 8 - Товары с остатком меньше 3
    elif choice == "8":
        print(f"Товары с остатком меньше 3:")
        found = False
        for name, products in warehouse.items():
            if products['quantity'] < 3:
                print(f"  {name}: остаток {products['quantity']} шт.")
                found = True
        if not found:
            print(f"  Таких товаров нет!")

    # 0 - Выход
    elif choice == "0":
        print(f"До свидания!")
        break

    else:
        print(f"Неверный выбор! Попробуйте снова.")