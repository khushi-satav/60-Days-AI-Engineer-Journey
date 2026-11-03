age = int(input('Enter your age: '))

if age >= 18:
    print('You can vote')

elif age>=101:
    print('greater than 100')
elif age<=0:
    print('invalid')    
else:
    print('error')