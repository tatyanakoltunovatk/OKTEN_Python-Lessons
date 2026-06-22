#- створити функцію яка обчислює та повертає площу прямокутника зі сторонами а і б
from unittest import result


def calc (a, b):
    rectangle_result = a * b
    print(f"\nArea of a rectangle with a={a} and b={b} is {rectangle_result}")
    return rectangle_result

calc(10, 45)
print('----------------')

#створити функцію яка обчислює та повертає площу кола з радіусом r
import math
def calc2(r):
    res = math.pi * r * r
    print(f"Area of circle with r={r} is {res}")
    return res

calc2(5)
print('--------------')

#створити функцію яка обчислює та повертає площу циліндру висотою h, та радіутом r
def calc3 (r, h):
    cylinder_result = (2 * math.pi * r * r) + (2 * math.pi * r * h)
    print(f"The cylinder with r={r} and h={h} has area={cylinder_result}")
    return cylinder_result

calc3(10.5, 8.7)
print('--------------')

#створити функцію яка приймає масив та виводить кожен його елемент
my_content = [11, 'sunny', 7, 'gold standard', 558, 25, 34, True]

def print_element_in_array (big_arr):
    for element in big_arr:
        print(element)

print_element_in_array(my_content)
print('-----------------')

#створити функцію sum(arr) яка приймає масив чисел,
# підсумовує значення елементів масиву та повертає його. Приклад sum([1,2,10]) //->13
def sum_numbers_in_array (arr_num):
    return sum(arr_num)

print("The sum of numbers in the array is", sum_numbers_in_array([22, 10, 5, 17, 30, 11, 9, 8, -50]))
