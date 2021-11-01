# -*- coding: utf-8 -*-
import re
from math import ceil
from time import sleep

import requests
from bs4 import BeautifulSoup
from selenium import webdriver


class Material:
    def __init__(self, title, img, features):
        self.title = title
        self.img = img
        self.features = features


def writeFileURL(URL, name_file):
    filePath = name_file
    f = open(filePath, 'a', encoding="utf-8")
    f.write(str(URL) + str("\n"))

def writeFileMaterial(title_name, image, features):
    filePath = r'C:\Users\Никита\Documents\Petrovich\Material.txt'
    f = open(filePath, 'a', encoding="utf-8")
    f.write(str(title_name) + "|" + str(image) + "|" + str(features) + str("\n"))


def get_html():
    a = open(r'C:\Users\Никита\Documents\Petrovich\URL.txt', 'r', encoding="utf-8")
    all_mat = a.read().\
        replace('\n', ',').\
        replace('\'', '').\
        replace('[', '').\
        replace(']', '').\
        replace(' ', '').\
        replace('', '').\
        split(',')

    for i in range(len(all_mat)):
        response = requests.get("https://petrovich.ru/catalog" + all_mat[i]).text

        soup = BeautifulSoup(response, "html.parser")

        title_name = soup.h1.text
        image = "https:" + soup.select("div.content-slide img")[0].attrs["data-src"]
        features = soup.select("ul.product-properties-list.listing-data li")
        print(i)
        for q in range(len(features)):
            features[q] = str(features[q]).replace("<li class=\"data-item\">", "") \
                .replace("<div class=\"title\">", "") \
                .replace("</div><div class=\"value\">", ": ") \
                .replace("</div></li>", "")\
                .replace("<span>", "")\
                .replace(" </span>", "")

        features_spr = {}

        for q in range(len(features)):
            lst = features[q].split(": ")
            features_spr.update({lst[0]: lst[1]})

        mat1 = Material(title_name, image, features_spr)

        writeFileMaterial(mat1.title, mat1.img, mat1.features)


def get_id_materials():
    all_mat = []
    a = open(r'C:\Users\Никита\PycharmProjects\pythonProject\materials\id_category.txt', 'r', encoding="utf-8")
    lst_url_sub_cat = a.read().replace('\n', ',').split(',')

    for i in range(len(lst_url_sub_cat)):
        response = requests.get("https://petrovich.ru/catalog" + str(lst_url_sub_cat[i])).text
        sout = BeautifulSoup(response, "html.parser")

        count_mat = find_count_page(int(
            re.findall('>Найдено товаров: <!-- -->(.*)</p>', str(sout.select("header.product-list-header p")))[0]))

        for q in range(count_mat):
            response = requests.get("https://petrovich.ru/catalog" + str(lst_url_sub_cat[i] + "?p=" + str(q))).text
            sout = BeautifulSoup(response, "html.parser")

            note_mat = sout.select("div.product-list a")

            c = re.findall('href="/catalog(.+?)"', str(note_mat))

            all_mat += c
            print(q + 1)
            print(count_mat)
            print(all_mat)
            if q + 1 == count_mat:
                writeFileURL(all_mat, r'C:\Users\Никита\Documents\Petrovich\URL.txt')
                all_mat.clear()


    return all_mat


def find_count_page(count_mat):
    return ceil(count_mat / 20)


def get_all_url_subCategory(url):
    response = requests.get(url).text
    sout = BeautifulSoup(response, "html.parser")
    writeFileURL(str(re.findall('href="/catalog(.+?)"', str(sout.select("div.product-list-container a.catalog-subsection")))).
                 replace('\'', '').
                 replace('[', '').
                 replace(']', '').
                 replace(' ', ''),
                 r'C:\Users\Никита\PycharmProjects\pythonProject\materials\id_category.txt')



def main():
    '''get_html(get_id_materials(get_all_url_subCategory("https://petrovich.ru/catalog/245635348/")))
    get_all_url_subCategory("https://petrovich.ru/catalog/" + str(245635348))
    get_all_url_subCategory("https://petrovich.ru/catalog/" + str(1313))
    get_all_url_subCategory("https://petrovich.ru/catalog/" + str(1384))
    get_all_url_subCategory("https://petrovich.ru/catalog/" + str(12088))
    get_all_url_subCategory("https://petrovich.ru/catalog/" + str(1533))
    get_all_url_subCategory("https://petrovich.ru/catalog/" + str(1366))
    get_all_url_subCategory("https://petrovich.ru/catalog/" + str(1336))
    get_all_url_subCategory("https://petrovich.ru/catalog/" + str(13381))
    '''

    #get_id_materials()
    get_html()


main()


def a():
    response = requests.get("https://petrovich.ru/catalog/1453/101923/").text

    soup = BeautifulSoup(response, "html.parser")

    title_name = soup.h1.text
    image = "https:" + soup.select("div.content-slide img")[0].attrs["data-src"]
    features = soup.select("ul.product-properties-list.listing-data li")
    writeFileMaterial(title_name, image, features)

# writeFile()
#a()


def getInfoFile():
    filePath = r'C:\Users\Никита\Documents\Petrovich\URL.txt'
    f = open(filePath, 'r', encoding="utf-8")
    a = f.read()
    a = a.split(',')
    print(a)

#getInfoFile()