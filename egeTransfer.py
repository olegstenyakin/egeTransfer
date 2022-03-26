#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""  
@file 
Модуль возращает итоговые баллы по стобалльной системе оценивания
в соответствии с набранными первичными баллами
на Едином государственном экзамене (ЕГЭ) по физике в 2022 году.

Используемый алгоритм описан в документе
«Распоряжение Рособрнадзора от 16.07.2019 № 1122-10 ... (в редакции от 02.07.2021 № 933-10)»,
доступный на официальной странице Рособрнадзора в разделе Документы -> Нормативно-правовые акты
https://obrnadzor.gov.ru/gia/gia-11/dokumenty/

Алгоритм модифицирован под изменившуюся шкалу оценивания в 2022 году,
и носит предварительный характер.

@author Олег Стенякин
@date 2022-03-24
"""


# Импорт
from math import ceil
from tabulate import tabulate

# Определяем промежуточные точки для первичных баллов
# и соответствующие им значения итоговых баллов 
points = {
    0 : 0,
    12 : 39, 
    33 : 62,
    54: 100
}

# Функция вычисляет значение итогового балла
# на соответствующем промежутке между 
def tb ( pb ) :
    if pb <= list(points.keys())[1] :
        k = points[list(points.keys())[1]] / list(points.keys())[1]
        l = 0
    elif pb <= list(points.keys())[2] :
        k = ( points[list(points.keys())[2]] - points[list(points.keys())[1]] ) / ( list(points.keys())[2] - list(points.keys())[1] )
        l = points[list(points.keys())[2]] - k * list(points.keys())[2]
    else :
        k = ( points[list(points.keys())[3]] - points[list(points.keys())[2]] ) / ( list(points.keys())[3] - list(points.keys())[2] )
        l = points[list(points.keys())[3]] - k * list(points.keys())[3]

    prec  = 5 
    test_point = round ( k * pb + l , prec ) 

    return test_point

# Функция запрашивает значение первичных баллов
# и возращает значение итоговых баллов
def test_value () : 
    pb = 0
    try :
        pb = int ( input( 'Какое количество первичных баллов вы набрали от 0 до 54: ') ) 
        if pb >= list(points.keys())[0] and pb <= list(points.keys())[3] :
            final = int( ceil ( tb( pb ) ) ) 
            print(f'Ваш итоговый балл: {final}!')
        else :
            print('Пожалуйста, введите целое число от 0 до 54 и попробуйте снова')
    except ( ValueError, TypeError, KeyError ) :
        print('Пожалуйста, введите целое число от 0 до 54 и попробуйте снова')
    except :
        print('\n')
        print('Произошло нечто странное, попробуйте снова')

# Функция выводит полную таблицу соответствия первичных и итоговых баллов
def table () :
    # заполняем список
    table_of_scores = []
    for i in range(list(points.keys())[0], list(points.keys())[3] + 1) :
        table_of_scores.append([i, int( ceil ( tb ( i ) ) )])
    
    # таблица из списка
    print( tabulate( table_of_scores, headers=['Первичные баллы', 'Итоговые баллы'], tablefmt='grid', numalign='center') )

if __name__ == '__main__':
    test_value () 

# END
