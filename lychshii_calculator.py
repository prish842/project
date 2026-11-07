a = float(input())
b = float(input())
znak = input()

if znak == "+":
    c = a + b
elif znak == "-":
    c = a - b
elif znak == "*":
    c = a * b
elif znak == "/":
    c = a / b
else:
    c = "Ошибка: неизвестный знак"

print(c)