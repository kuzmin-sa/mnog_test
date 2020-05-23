#Задание 4 "Словарь с рандомной выдачей"

import random

amount_of_words = input("Как много слов вы хотите занести в словарь \n:")
aow = int(amount_of_words)
slovar = {}

for i in range(aow):
    key = input("Введите слово на английском \n:")
    value = input("Введите слово на русском \n:")
    slovar[key] = value

keys = list(slovar.keys())
random.shuffle(keys)

Shuffledslovar = dict()
for key in keys:
  Shuffledslovar.update({key:slovar[key]})

for key in Shuffledslovar.keys():
    print("Переведи слово", key, ": ")
    answer = input("Ваш вариант перевода\n:")
    if Shuffledslovar[key] == answer:
        print("Все верно!")
    else:
        print("А правильный овет был", Shuffledslovar[key])