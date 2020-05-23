#Задание 5 "Финансовый учет"

with open('fa.txt') as file:
    lines = file.readlines()

num = [int(line) for line in lines]

maximum = ("Максимальное значение в файле: " + str(max(num)))
minimum = ("Максимальное значение в файле: " + str(min(num)))
summa = ("Сумма значений в файле: " + str(sum(num)))
average = ("Среднее значение в файле: " + str((sum(num) / len(num))))

print(maximum)
print(minimum)
print(summa)
print(average)

lines = [maximum, minimum, summa, average]

with open("fa_result.txt", "w") as f:
    for line in lines:
        f.write(str(line) + '\n')