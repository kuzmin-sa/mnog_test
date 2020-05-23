#Задание 6 "Число Пи"

filename = 'pi_million_digits.txt'
with open(filename) as file:
    lines = file.readline()
pi_string = ''
for line in lines:
    pi_string += line


birthday = input("Введите дату рождения: ")
if birthday in pi_string:
    print("Вам повезло!")
    indexs = pi_string.index(birthday) + 1
    print("Ваш день рождения начинается с " + str(indexs) + " цифры числа Пи!")
else:
    print("Не переживайте, вы не один такой, кто не попал в список(")