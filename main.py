import csv
import datetime
import inspect
import os
from itertools import cycle
from math import sqrt
from random import randint
from time import sleep

from PIL import Image, ImageDraw


def arithmetic(num1, num2, fn):
    if fn == "+":
        return num1 + num2
    elif fn == "-":
        return num1 - num2
    elif fn == "*":
        return num1 * num2
    elif fn == "/":
        return num1 / num2
    else:
        return "Неизвестная операция"


def is_year_leap(year):
    if year % 4 == 0:
        return True
    else:
        return False


def square(side):
    perimetr = side * 4
    square_box = side ** 2
    diagonal = side * sqrt(2)
    return (perimetr, square_box, diagonal)


def season(mounth):
    if mounth in [12, 1, 2]:
        return "зима"
    elif mounth in [3, 4, 5]:
        return "весна"
    elif mounth in [6, 7, 8]:
        return "лето"
    elif mounth in [9, 10, 11]:
        return "осень"


def bank(amount, year):
    bet = 0.1
    i = 0
    while i != year:
        amount += (amount * bet)
        i += 1

    return amount


# def is_prime():
#    list_numbs = list(range(1, 1000))
#
#    for i in list_numbs:
#        if i % list_numbs[] != 0:
#            print(i)
#    return list_numbs


def more_than_five(lst):
    lst_result = []
    for i in lst:
        if abs(i) > 5:
            lst_result.append(i)
    return lst_result


def replace_upper_char():
    letters = 'ЫгВЫоЯСремДШНККАыкЩЙФа'

    for letter in letters:
        if letter.upper() == letter:
            letters = letters.replace(letter, '')

    print(letters)


def create_alfabet():
    alfa = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"

    for i in range(11):
        print("^" * 27)
        for q in alfa:
            if alfa.index(q) % 11 == i:
                print('| ', q.upper(), q, ' |', end='')
        print()
    print('^' * 27)


def auto():
    while True:
        name_user = input()
        lst_name = ["Мавпродош", "Лорнектиф", "Древерол", "Фиригарпиг", "Клодобродыч"]
        if name_user in lst_name:
            print("good")
            break
        else:
            print("bad")


def all_divisors(number):
    lst_result = []
    lst_num = range(1, number + 1)
    for i in lst_num:
        if number % i == 0:
            lst_result.append(i)

    return lst_result


def sum_range(start, end):
    if start > end:
        _x = start
        start = end
        end = _x

    lst = range(start, end + 1)

    return sum(lst)


class Soda:

    def __init__(self, supplement):
        if isinstance(supplement, str):
            self.supplement = supplement
        else:
            self.supplement = None

    def show_my_drink(self):
        if self.supplement:
            print("Газировка и " + self.supplement)
        else:
            print("Обычная газировка")


class Nikolay:
    __slots__ = ["name", "age"]

    def __init__(self, name):
        self.name = name
        if self.name != "Николай":
            self.name = "Я не Максим, а Николай"

    def printname(self):
        print(self.name)


def read_last(lines, file):
    a = open(file, encoding="utf-8")
    lst = a.readlines()
    for line in lst[-lines:]:
        print(line.strip())


def show_dir(path):
    print(os.listdir(path))


def longest_words(file):
    lst_str_max_len = []
    lst = open(file, encoding="utf-8").read().split()

    max_len = len(max(lst, key=len))

    for i in lst:
        if max_len < len(i) or max_len == len(i):
            lst_str_max_len.append(i)

    return (lst_str_max_len)


def create_csv_file(path):
    with open(path, "w", encoding="utf-8", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(['№', 'Секунда ', 'Микросекунда'])

        for line in range(1, 300):
            writer.writerow([line, datetime.datetime.now().second, datetime.datetime.now().microsecond])
            sleep(0.01)


def circles_generator(num_of_circles=100):
    path = r"C:\Users\Никита\Desktop\circles"

    if not os.path.exists('circles'):
        os.mkdir(path)

    for name_img in range(1, 300):

        img = Image.new("RGB", (600, 600), (255, 255, 255))
        idraw = ImageDraw.Draw(img)
        idraw.ellipse((0, 0, 600, 600), fill=(randint(0, 255), randint(0, 255), randint(0, 255)))

        img.save(fr"C:\Users\Никита\Desktop\circles\{name_img}.jpg" , quality=85)

    img_new = Image.open(r"C:\Users\Никита\Desktop\h-23943.jpg")
    b_and_w = img_new.convert('L')
    b_and_w.show()



def infinite(lst, tries):

    numbers = cycle(lst)
    i = 0
    str_result = ""
    if lst:
        while i != tries:
            str_result += str(next(numbers))
            i += 1
    return str_result


def find_gip():
    while True:
        kat_1 = int(input())
        kat_2 = int(input())

        gip = sqrt(kat_1 ** 2 + kat_2 ** 2)
        print(gip)



def find_rag():
    while True:

        a = input()
        b = input()
        c = input()

        try:
            if a == None:
                a = 0
            else:
                a = int(a)

            if b == None:
                b = 0
            else:
                b = int(b)

            if c == None:
                c = 0
            else:
                c = int(c)


            D = b ** 2 - 4 * a * c

            if D < 0:
                print("Корней нет")
            elif D > 0:
                x1 = -b+sqrt(D)/2*a
                x2 = -b-sqrt(D)/2*a
                print("Корень_1: " + str(x1))
                print("Корень-2: " + str(x2))
            else:
                x = -b/2*a
                print("Корень: " + str(x))
        except:
            print("Error")




def create_multiplication_tables():
    M = int(input())
    a = int(input())
    b = int(input())

    for i in range(a - 1, b):
        print(str(M) + "*" + str(a) + "=" + str(M*a))
        a +=1

def is_simple_num():
    num = int(input())
    is_simle = True

    for i in range(2, num-1):
        if num % i == 0:
            is_simle = False
    return print(is_simle)


def dio_simple_num():
    num = int(input())
    is_simle = True
    lst = []

    for i in range(2, num-1):
        for q in range(2, i-1):
            if i % q == 0:
                break
            else: lst.append(i)
            break
    return print(lst)


def crate_lst():
    min_num = int(input())
    max_num = int(input())
    len_lst = int(input())

    lst = []

    for i in range(len_lst):
        lst.append(randint(min_num, max_num))


def sort_lst():
    lst = [1,5,77,83,3,5,63,23,5,1]

    #i = 0
    for i in range(len(lst)):
        for q in range(len(lst)-1):
            if lst[q] > lst[q+1]:
                lst[q], lst[q+1] = lst[q+1], lst[q]
            q +=1
    print(lst)

sort_lst()

