# number = 5
# print(number)
#
# message = 'Hello!'
# print(id(message))
#
# num1 = 5
# num2 = '6'
# print(num1 + int(num2))
#
# quantity = 5
# items = 'books'
# print(str(quantity) + ' ' + 'books')
#
# print(5+2)
# print(5-2)
# print(5*2)
# print(5**2)
# print(5/2)
# print(5//2)
# print(5%2)

message = input('Please provide a value: ')
print(message)

# number = input('How old are you? ')
number = int(input('How old are you? '))
print(f'Your age is: {number}')
print('Your age is : ' + str(number))

from lesson2 import sum_it
print(sum_it(100, 200))
