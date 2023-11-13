import tkinter as tk  # Вызываю модуль для создания интерфейса программы


# Функция для вычисления закона кулона в зависимости от вопроса
def calculate_coulombs_law(question):
    if question == 1:
        try:
            result_text.set('')  # Очистка результата

            k = int(k_var.get())  # Получение значения k из поля ввода
            q1 = int(q1_var.get())  # Получение значения |q1| из поля ввода
            q2 = int(q2_var.get())  # Получение значения |q2| из поля ввода
            r_squared = int(r_squared_var.get())  # Получение значения r^2 из поля ввода

            # Вычисление силы по закону кулона и установка результата
            calc_coulomb = k * ((abs(q1) * abs(q2)) / (r_squared))
            result_text.set(f'F = {k} * ((|{q1}| * |{q2}|) / ({r_squared})) = {calc_coulomb}')
        except TypeError:
            clear_fields()
    elif question == 2:
        try:
            result_text.set('')  # Очистка результата

            k = int(k_var.get())  # Получение значения k из поля ввода
            q1 = int(q1_var.get())  # Получение значения |q1| из поля ввода
            q2 = int(q2_var.get())  # Получение значения |q2| из поля ввода
            r_squared = int(r_squared_var.get())  # Получение значения r^2 из поля ввода
            e = int(e_var.get())  # Получение значения E0 из поля ввода

            # Вычисление силы в среде и установка результата
            calc_coulomb = (k * abs(q1) * abs(q2)) / (e * r_squared)
            result_text.set(f'F = ({k} * |{q1}| * |{q2}|) / ({e} * {r_squared}) = {calc_coulomb}')
        except TypeError:
            clear_fields()
    elif question == 3:
        try:
            result_text.set('')  # Очистка результата

            e = int(e_var.get())  # Получение значения E0 из поля ввода

            # Вычисление K и установка результата
            k_value = 1 / (4 * 3.14 * e)
            result_text.set(f'K = 1 / (4 * 3.14 * {e}) = {k_value}')
        except TypeError:
            clear_fields()


# Функция для очистки полей ввода
def clear_fields():
    question_var.set('')  # Очистка переменных вопроса
    k_var.set('')  # Очистка поля ввода k
    q1_var.set('')  # Очистка поля ввода |q1|
    q2_var.set('')  # Очистка поля ввода |q2|
    r_squared_var.set('')  # Очистка поля ввода r^2
    e_var.set('')  # Очистка поля ввода E0
    result_text.set('')  # Очистка результата


root = tk.Tk()  # Создание основного окна Tkinter
root.title("Калькулятор закона кулона")  # Установка заголовка окна (названия окна)

k_label = tk.Label(root, text='Введите K:')  # Создание метки для поля ввода k
k_label.pack()  # Размещение метки в окне

k_var = tk.StringVar()  # Создание переменной типа StringVar для хранения значения k
k_entry = tk.Entry(root, textvariable=k_var)  # Создание поля ввода, связанного с k_var
k_entry.pack()  # Размещение поля ввода в окне

q1_label = tk.Label(root, text='Введите |q\u2081|:')  # Создание метки для поля ввода |q1|
q1_label.pack()  # Размещение метки в окне

q1_var = tk.StringVar()  # Создание переменной типа StringVar для хранения значения |q1|
q1_entry = tk.Entry(root, textvariable=q1_var)  # Создание поля ввода, связанного с q1_var
q1_entry.pack()  # Размещение поля ввода в окне

q2_label = tk.Label(root, text='Введите |q\u2082|:')  # Создание метки для поля ввода |q2|
q2_label.pack()  # Размещение метки в окне

q2_var = tk.StringVar()  # Создание переменной типа StringVar для хранения значения |q2|
q2_entry = tk.Entry(root, textvariable=q2_var)  # Создание поля ввода, связанного с q2_var
q2_entry.pack()  # Размещение поля ввода в окне

r_squared_label = tk.Label(root, text='Введите r\u00b2:')  # Создание метки для поля ввода r^2
r_squared_label.pack()  # Размещение метки в окне

r_squared_var = tk.StringVar()  # Создание переменной типа StringVar для хранения значения r^2
r_squared_entry = tk.Entry(root, textvariable=r_squared_var)  # Создание поля ввода, связанного с r_squared_var
r_squared_entry.pack()  # Размещение поля ввода в окне

e_label = tk.Label(root, text='Введите E\u2080:')  # Создание метки для поля ввода E0
e_label.pack()  # Размещение метки в окне

e_var = tk.StringVar()  # Создание переменной типа StringVar для хранения значения E0
e_entry = tk.Entry(root, textvariable=e_var)  # Создание поля ввода, связанного с e_var
e_entry.pack()  # Размещение поля ввода в окне

clear_button = tk.Button(root, text='Очистить поля',
                         command=clear_fields)  # Создание кнопки "Очистить поля" с функцией clear_fields
clear_button.pack()  # Размещение кнопки в окне

result_text = tk.StringVar()  # Создание переменной типа StringVar для отображения результата
result_label = tk.Label(root,
                        textvariable=result_text)  # Создание метки для отображения результата, связанной с result_text
result_label.pack()  # Размещение метки результата в окне

question_label = tk.Label(root, text='Выберите операцию::')  # Создание метки "Выберите операцию:"
question_label.pack()  # Размещение метки в окне

question_var = tk.IntVar()  # Создание переменной типа IntVar для хранения выбора операции

option1_button = tk.Button(root, text='узнать F вакуума', command=lambda: calculate_coulombs_law(
    1))  # Создание кнопки "узнать F вакуума" с функцией calculate_coulombs_law(1)
option1_button.pack()  # Размещение кнопки в окне

option2_button = tk.Button(root, text='узнать F в среде', command=lambda: calculate_coulombs_law(
    2))  # Создание кнопки "узнать F в среде" с функцией calculate_coulombs_law(2)
option2_button.pack()  # Размещение кнопки в окне

option3_button = tk.Button(root, text='узнать K', command=lambda: calculate_coulombs_law(
    3))  # Создание кнопки "узнать K" с функцией calculate_coulombs_law(3)
option3_button.pack()  # Размещение кнопки в окне

root.geometry("300x350")  # Установка размера окна (ширина x высота)
root.mainloop()  # Запуск главного цикла Tkinter
