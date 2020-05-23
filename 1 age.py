#Задание 1 "Калькулятор возраста"

print("Калькулятор возраста")

year_of_birth = input("Введите год вашего рождения: ")
year = input("Введите год для расчета возраста: ")

years_old = int(year) - int(year_of_birth)

print("В " + str(year) + " году вам будет: " + str(years_old))