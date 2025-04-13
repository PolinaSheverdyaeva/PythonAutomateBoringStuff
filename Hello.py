print("Hello World!")
print("What is your name?")
myName = input().strip().capitalize() #strip spaces and capitalize
print('It is good to meet you, ' + myName)
print('The length of your name is: ')
print(len(myName))
print('What is your age?')
myAge = input().strip()
if myAge.isdigit():
    myAge = int(myAge)
else:
    print("Error")
print('You will be ' + str(int(myAge) + 1) + ' in a year.')
print('spam' + 'spamspam')
print('spam' * 3)

