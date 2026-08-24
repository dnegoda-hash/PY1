# def add(x, y):
#     return x + y
#
# def subtract(x, y):
#     return x - y
#
# def multiply(x, y):
#     return x * y
#
# def divide(x, y):
#     if y == 0:
#         return "Ошибка: Деление на ноль"
#     return x / y
#
# def log(result):
#     with open("calculations.txt", "a") as file:
#         file.write(result + "\n")
#
# # Новая функция для просмотра истории
# def show_history():
#     try:
#         with open("calculations.txt", "r") as file:
#             lines = file.readlines()
#             if not lines:
#                 print("История пуста.")
#             else:
#                 print("История вычислений:")
#                 for line in lines:
#                     print(line.strip())
#     except FileNotFoundError:
#         print("Файл истории не найден. Вы еще не совершали вычислений.")
#
# print("Выберите операцию: ")
# print("1. Сложение")
# print("2. Вычитание")
# print("3. Умножение")
# print("4. Деление")
# print("5. Просмотр истории вычислений")
#
# choice = input("Введите номер операции (1/2/3/4/5): ")
#
# if choice == '5':
#     show_history()
# else:
#     # Блок ввода чисел выполняется только если выбрана операция 1-4
#     try:
#         num1 = float(input("Введите первое число: ")) # Используем float для поддержки дробных чисел (как 1.00 на скрине)
#         num2 = float(input("Введите второе число: "))
#
#         if choice == '1':
#             # Приводим к int для красоты вывода, если число целое, иначе оставляем float
#             n1 = int(num1) if num1.is_integer() else num1
#             n2 = int(num2) if num2.is_integer() else num2
#             res = add(num1, num2)
#             r_res = int(res) if res.is_integer() else res
#             r = f"Результат: {n1} + {n2} = {r_res}"
#             print(r)
#             log(r)
#
#         elif choice == '2':
#             n1 = int(num1) if num1.is_integer() else num1
#             n2 = int(num2) if num2.is_integer() else num2
#             res = subtract(num1, num2)
#             r_res = int(res) if res.is_integer() else res
#             r = f"Результат: {n1} - {n2} = {r_res}"
#             print(r)
#             log(r)
#
#         elif choice == '3':
#             n1 = int(num1) if num1.is_integer() else num1
#             n2 = int(num2) if num2.is_integer() else num2
#             res = multiply(num1, num2)
#             r_res = int(res) if res.is_integer() else res
#             r = f"Результат: {n1} * {n2} = {r_res}"
#             print(r)
#             log(r)
#
#         elif choice == '4':
#             n1 = int(num1) if num1.is_integer() else num1
#             n2 = int(num2) if num2.is_integer() else num2
#             res = divide(num1, num2)
#             # Для деления оставляем форматирование как есть или float
#             r = f"Результат: {n1} / {n2} = {res}"
#             print(r)
#             log(r)
#
#         else:
#             print("Неверный ввод")
#
#     except ValueError:
#         print("Ошибка: Введите корректное число.")

# Функции для математических операций
# def add(x, y):
#     return x + y
#
#
# def subtract(x, y):
#     return x - y
#
#
# def multiply(x, y):
#     return x * y
#
#
# def divide(x, y):
#     if y == 0:
#         return "Ошибка: Деление на ноль"
#     return x / y
#
#
# # Функция для сохранения результата в файл
# def log(result):
#     with open("calculations.txt", "a") as file:
#         file.write(result + "\n")
#
#
# # НОВАЯ ФУНКЦИЯ: Просмотр истории
# def show_history():
#     print("История вычислений:")
#     try:
#         # Открываем файл для чтения
#         with open("calculations.txt", "r") as file:
#             # Читаем все строки и выводим их
#             content = file.read()
#             if content:
#                 print(content)
#             else:
#                 print("Файл пуст.")
#     except FileNotFoundError:
#         # Если файла нет (программу запустили первый раз)
#         print("История пока пуста.")
#
#
# # --- Основная программа ---
#
# print("Выберите операцию: ")
# print("1. Сложение")
# print("2. Вычитание")
# print("3. Умножение")
# print("4. Деление")
# print("5. Просмотр истории вычислений")  # Добавили пункт 5
#
# choice = input("Введите номер операции (1/2/3/4/5): ")
#
# # Если выбрали 5, показываем историю и завершаем
# if choice == '5':
#     show_history()
#
# # Если выбрали 1-4, делаем вычисления
# elif choice == '1' or choice == '2' or choice == '3' or choice == '4':
#     num1 = int(input("Введите первое число: "))
#     num2 = int(input("Введите второе число: "))
#
#     if choice == '1':
#         r = f"Результат: {num1} + {num2} = {add(num1, num2)}"
#         print(r)
#         log(r)
#
#     elif choice == '2':
#         r = f"Результат: {num1} - {num2} = {subtract(num1, num2)}"
#         print(r)
#         log(r)
#
#     elif choice == '3':
#         r = f"Результат: {num1} * {num2} = {multiply(num1, num2)}"
#         print(r)
#         log(r)
#
#     elif choice == '4':
#         r = f"Результат: {num1} / {num2} = {divide(num1, num2)}"
#         print(r)
#         log(r)
#
# else:
#     print("Неверный ввод")

# Функция для сложения
def add(x, y):
    return x + y


# Функция для вычитания
def subtract(x, y):
    return x - y


# Функция для умножения
def multiply(x, y):
    return x * y


# Функция для деления
def divide(x, y):
    if y == 0:
        return "Ошибка: Деление на ноль"
    return x / y


# Функция для записи в файл
def log(result):
    file = open("calculations.txt", "a")
    file.write(result + "\n")
    file.close()


# Функция для просмотра истории
def show_history():
    try:
        file = open("calculations.txt", "r")
        lines = file.readlines()
        file.close()

        if len(lines) == 0:
            print("История пуста.")
        else:
            print("История вычислений:")
            for line in lines:
                print(line.strip())
    except:
        print("История пуста.")


# Вывод меню
print("Выберите операцию:")
print("1. Сложение")
print("2. Вычитание")
print("3. Умножение")
print("4. Деление")
print("5. Просмотр истории")

# Ввод выбора пользователя
choice = input("Введите номер операции (1/2/3/4/5): ")

# Если пользователь хочет посмотреть историю
if choice == '5':
    show_history()

# Если пользователь выбрал операцию 1-4
elif choice == '1' or choice == '2' or choice == '3' or choice == '4':
    # Ввод чисел
    num1 = float(input("Введите первое число: "))
    num2 = float(input("Введите второе число: "))

    # Выполнение операции в зависимости от выбора
    if choice == '1':
        result = add(num1, num2)
        symbol = "+"
    elif choice == '2':
        result = subtract(num1, num2)
        symbol = "-"
    elif choice == '3':
        result = multiply(num1, num2)
        symbol = "*"
    elif choice == '4':
        result = divide(num1, num2)
        symbol = "/"

    # Форматирование чисел для красивого вывода (убираем .0 у целых чисел)
    if num1 == int(num1):
        num1 = int(num1)
    if num2 == int(num2):
        num2 = int(num2)
    if isinstance(result, float) and result == int(result):
        result = int(result)

    # Создание строки с результатом
    output = "Результат: " + str(num1) + " " + symbol + " " + str(num2) + " = " + str(result)

    # Вывод на экран и запись в файл
    print(output)
    log(output)

# Если пользователь ввел что-то другое
else:
    print("Неверный ввод")