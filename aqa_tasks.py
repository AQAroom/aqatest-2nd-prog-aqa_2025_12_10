# Написать программу, которая
# принимает от пользователя два числа и знак операции,
# после чего применяет эту операцию к введенным числам.
a = int(input())
b = int(input())
c = input()
if c == "+":
    print(a + b)
elif c == "-":
    print(a - b)
elif c == "*":
    print(a * b)
elif c == "/":
    print(a / b)
elif c == "^":
    print(a ** b)
else:
    print("Неизвестная операция")
