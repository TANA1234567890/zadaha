# Простейший калькулятор.
#Обработать ошибку "деление на ноль"
a = float(input("Введите первое число: "))
b = float(input("Введите второе число: "))
c = input("Введите знак действия: ")
if c == "+":
    print(a+b)
elif c == "-":
    print(a-b)
elif c == "*":
    print(a*b)
elif c == "/" and b != 0:
    print(a/b)
else:
    print("Делить на ноль нельзя")

