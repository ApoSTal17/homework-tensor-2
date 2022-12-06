a, b = map(str, input("Введите 2 вещ. или целых числа через пробел: ").split())
lst = []

for i in [a, b]:
    if '.' in i:
        lst.append(float(i))
    else:
        lst.append(int(i))

a, b = lst

print(f'Сложение a, b: {a + b}')
print(f'Вычитание a, b: {a - b}')
print(f'Умножение a, b: {a * b}')
print(f'Деление a, b: {a / b}')
print(f'Возведение в степень (a^b): {a ** b}')
print(f'Деление по модулю (a mod b): {a % b}')
print(f'Целочисленное деление: {a // b}')