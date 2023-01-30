#Дано натуральное число N. Найдите значение выражения:N + NN + NNN
#N может быть любой длины.

number = input('Введите число N: ')
number = str(number)
l=str('')
list = []
print(type(number))
for _ in range(3):
    l = l + number
    list.append(l)
    print(l, end=" "  '\n')
print(list)
result = int(list[0]) + int(list[1]) + int(list[2])
print(f' значение выражения:N + NN + NNN = {result} ')