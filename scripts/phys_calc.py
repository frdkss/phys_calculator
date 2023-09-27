import os
import numpy as np
import matplotlib as mpl


def law_energy_save():
    q_count = int(input('Введите количество q: '))
    for i in range(q_count):
        q = int(input('Введите q: '))
        q += q
    print(q)


def law_culon():
    question = int(input(
        'Напишите 1 если хотите узнать F вакуума \nНапишите 2 если F в среде \nНапишите 3 если K неизвестно\nВведите число: '))
    if question == 1:
        os.system('cls||clear')
        culon_law = u'Закон кулона: \nF = k * ((|q\u2081|*|q\u2082|)/(r\u00b2))\n'
        print(culon_law)
        k = int(input('Введите k: '))
        q1 = int(input('Введите |q\u2081|: '))
        q2 = int(input('Введите |q\u2082|: '))
        r = int(input('Введите r\u00b2: '))
        calc_culon = k * ((q1 * q2) / (r ** 2))
        culon_quest = f'F = {k} * (({q1}\u2081*{q2}\u2082)/({r}\u00b2))'
        print(f'\n{culon_quest}\n{calc_culon}')
        return law_culon()
    elif question == 2:
        os.system('cls||clear')
        print('F = (K*|q\u2081|*|q\u2082|)/(e*r\u00b2)')
        k = int(input('Введите k: '))
        q1 = int(input('Введите |q\u2081|: '))
        q2 = int(input('Введите |q\u2082|: '))
        r = int(input('Введите r\u00b2: '))
        e = int(input('Введите E\u2080: '))
        print(f'F = ({k}*|{q1}|*|{q2}|)/({e}*{r})')
        print(f'F = {(k * q1 * q2) / (e * r)}')
        return law_culon()
    elif question == 3:
        os.system('cls||clear')
        print(f'K = 1/(4*3.14*E)\u2080)')
        e = int(input('Введите E\u2080: '))
        print(f'K = 1/(4*3.14*{e})')
        print(f'K = {1 / (4 * 3.14 * e)}')
        return law_culon()
    elif question == 0:
        exit()
    else:
        return law_culon()


# law_energy_save()
law_culon()
