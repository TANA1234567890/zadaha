# Задача 7.
# Массив из 7 цифр. Если четных цифр в нем больше, чем нечетных,
# то найти сумму всех его цифр, если нечетных больше,
# то найти произведение 3 и 6 элементов
mas = [1, 2, 3, 4, 5, 6, 7]
print("Данный массив: ", mas)
mas1 = [] #массив четных чисел
mas2 = [] #массив нечетных чисел
s1 = 0 # сумма
p2 = 1 # произведение
for i in mas:
    if i % 2 == 0:
        mas1.append(i)
    elif i % 2 != 0:
        mas2.append(i)
print("четные цифры: ", mas1)
print("нечетныуе цифры: ", mas2)
print("количество четных цифр: ", len(mas1))
print("количество нечетных цифр: ", len(mas2))
if len(mas1) > len(mas2):
    for i in mas:
        s1 = s1 + i
    print("сумма всех цифр данного массива: ", s1)
else:
    p2 = mas[0] * mas[2] * mas[5]
    print("произведение 1,3 и 6 элемента данного массива: ", p2)
