import requests
# import json
# import pprint
from tkinter import *
from tkinter import ttk
from tkinter import messagebox as mb


def update_currency_label(event):
    code = target_combobox.get()
    name = currencies[code]
    currency_label.config(text=name)


def update_currency_label2(event):
    code = base2_combobox.get()
    name = currencies[code]
    currency_label2.config(text=name)


def exchange():
    # code = entry.get().strip().upper()
    target_code = target_combobox.get()
    base_code = base_combobox.get()
    base2_code = base2_combobox.get()
    if target_code and base_code:
        try:
            result = requests.get(f"https://open.er-api.com/v6/latest/{base_code}")
            result.raise_for_status()
            # data = json.loads(result.text)
            data = result.json()

            result2 = requests.get(f"https://open.er-api.com/v6/latest/{base2_code}")
            result2.raise_for_status()
            data2 = result2.json()

            if target_code in data['rates'] and target_code in data2['rates']:
                exchange_rate = data['rates'][target_code]
                exchange_rate2 = data2['rates'][target_code]
                base = currencies[base_code]
                base2 = currencies[base2_code]
                target = currencies[target_code]

                mb.showinfo('Курс обмена',
                            f'Курс {base}:\n'
                            f'  {exchange_rate:.1f} {target} за 1 {base_code}\n\n'
                            f'Курс {base2}:\n'
                            f'  {exchange_rate2:.1f} {target} за 1 {base2_code}')
            else:
                mb.showerror('Ошибка', f'Валюта {target_code} не найдена')


        except Exception as e:
            mb.showerror('Ошибка', f'error 400 {e}')


# result = requests.get("https://open.er-api.com/v6/latest/USD")
# data = json.loads(result.text)
# # print(data)
# # print(type(data))
# # for item in data.items():
# #     print(item)
# p = pprint.PrettyPrinter(indent=4)
# p.pprint(data)
currencies = {
    "USD": "Доллар США",
    "EUR": "Евро",
    "CNY": "Юань",
    "RUB": "Российский рубль",
}

pop_curr = ['EUR', 'USD', 'RUB', 'CNY']

root = Tk()
# root.title("Курс валют по отношению к доллару США")
root.title("Курс валют ")
root.geometry("350x320")
Label(text='Базовая валюта').pack(pady=10, padx=10)
base_combobox = ttk.Combobox(values=list(currencies.keys()))
base_combobox.pack()

Label(text='Вторая базовая валюта').pack(pady=10, padx=10)
base2_combobox = ttk.Combobox(values=list(currencies.keys()))
base2_combobox.pack()

currency_label2 = ttk.Label()
currency_label2.pack(pady=10, padx=10)

Label(text='Целевая валюта').pack(pady=10, padx=10)
target_combobox = ttk.Combobox(values=list(currencies))
target_combobox.pack()

currency_label = ttk.Label()
currency_label.pack(pady=10, padx=10)
# entry = Entry(width=10)
# entry.pack()
button = Button(text='Получить курс', command=exchange)
button.pack()
target_combobox.bind("<<ComboboxSelected>>", update_currency_label)
base2_combobox.bind("<<ComboboxSelected>>", update_currency_label2)
root.mainloop()