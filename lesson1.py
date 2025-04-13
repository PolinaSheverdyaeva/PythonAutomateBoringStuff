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

print(2 + 3 * 6)
print((2 + 3) * 6)
print(2 ** 8)
print(23 / 7)
print(23 // 7)
print(23 % 7)
print((5 - 1) * ((7 + 1) / (3 - 1)))

# Spam variable
spam = 40
print('Spam ' + str(spam))
eggs = 2
print('Eggs ' + str(eggs))
print(f'spam + eggs = {spam + eggs}')
print(f'spam + eggs + spam = {spam + eggs + spam}')
print(f'spam = spam + 2 = {spam + 2}')
spam = 'Hello'
print(f'spam = {spam}')
spam = 'Goodbye'
print(f'spam = {spam}')


