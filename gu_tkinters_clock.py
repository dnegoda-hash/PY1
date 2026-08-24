from time import strftime
from tkinter import *



def tick():
    current_time = strftime('%H:%M:%S')
    text.config(text=current_time)
    text.after(1000, tick)
# from генератор import result
def res(event=None):
    item = entry.get().strip()
    try:
        item = int(item) + 100
    except ValueError:
        item = 'Free'

    result.config(text=item)


root = Tk()
root.config(bg='black')
WIDTH = root.winfo_screenwidth()
HEIGHT = root.winfo_screenheight()
X = 400
Y = 250
root.geometry(f"{X}x{Y}+{WIDTH // 2 - X // 2}"
              f"+{HEIGHT // 2 - Y // 2 - 20}")
root.title('Будильник')

text = Label(root, text='00:00:00')
text.config(font=('Arial, 50'), bg='black', fg='lime')
text.pack()
entry = Entry(root, font=('Arial', 20), width=10, justify=CENTER)
entry.pack(pady=10)
entry.focus_set()
# result = Label(root, text='   ' * 10, bg='light gray', font=('Arial, 20'))
# result.config(justify=CENTER)
# result.pack()
btn = Button(text='Включить', width=10, font=('Arial', 10))
btn.pack(pady=5)
btn = Button(text='Выключить', width=10, font=('Arial', 10))
btn.pack(pady=5)
# entry.bind('<Return>', res)

# text1 = Label(root, text='Введите значение1: ')
# text1.pack()
tick()


root.mainloop()