# num = 6
# if num == 5:
#     print('Five!')
# elif num < 5:
#     print('Less than five')
# else:
#     print('More than five')

# num = 20
# if num > 10 and num < 100:
#     print("True")
#
# message1 = 'hello'
# message2 = 'hellohello'
# if len(message1) > len(message2):
#     print(message1)
# else:
#     print(message1)

# i = 5
# while i > 0:
#     print(i, 'Hello')
#     i = i -1
# print('Go!')

# i = 0
# while i < 5:
#     i = i + 1
#     print(i)
#     if i == 3:
#         break

# i = 0
# # while i < 5:
# #     i = i + 1
# #     if i == 3:
# #         continue
# #     print(i)

#  i = 5
#  while i > 0:
#     print(i, 'Hello')
# i = i - 1
# print('Go!')

# i = 0
# while i < 5:
#     i = i + 1
#     if i == 3:
#         continue
#     print(i)

# for i in range(10):
#     print(i)

# for i in range(1, 11, 2):
#     print(i)
#
# word = 'hello'
# for symbol in word:
#     print(symbol)
#
# word = 'hello'
# for symbol in word:
#     print(f'{word.index(symbol)} - {symbol}')

name = input('Enter your name')
for symbol in name:
    print(f'index {name.index(symbol)} - {symbol}')


print(bool(0.0))

# def sum_it(x, y):
#     result = x + y
#     return result
#
# print(sum_it(110, 200))
# result = sum_it(58, 79)

def sum_it(x, y):
    result = x + y
    yield result
    print('Finish work')

print(sum_it(100, 120))

