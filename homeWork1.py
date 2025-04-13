print('#2')
print('Hello World!')

print('#3')
user_name = input('Please provide your name: ')
print('Hello ' + str(user_name) + '!')

print('#4')
num1 = input('Please provide first number: ')
num2 = input('Please provide second number: ')
result = int(num1) ** int(num2)
print("Result of raising Num1 to the power of Num2: " + str(result))

print('#1.2')
# 1) Напишите программу, чтобы вывести:
#
# *********
# *       *
# *       *
# *********

print('*********')
print('*       *')
print('*       *')
print('*********')

print('#1.3')
# Напишите программу для нахождения цифр четырёхзначного числа. Число вводится при помощи методa input()
#
# Пример:
#
# Input: 3498
#
# Output:
# Тысячи - 3
# Сотни - 4
# Десятки - 9
# Единицы - 8

inp = input('Please enter 4 digits number: ')
num1 = int(inp) // 1000
mod1 = int(inp) % 1000

num2 = mod1 // 100
mod2 = mod1 % 100

num3 = mod2 // 10
mod3 = mod2 % 10

print('Тысячи - ' + str(num1))
print('Сотни - ' + str(num2))
print('Десятки - ' + str(num3))
print('Единицы - ' + str(mod3))

print('#1.4')
a = int(input('Please provide a number: '))
b = int(input('Please provide b number: '))

res1 = (a + b) ** 2
res2 = a ** 2 + b ** 2
print('Квадрат суммы 3 и 2 равен ' + str(res1))
print('Сумма квадратов 3 и 2 равна ' + str(res2))







