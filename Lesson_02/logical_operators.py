# Function to get data for input of the user

n1 = int(input('insert number: '))

if (n1 >= 0) and (n1 <= 5):
    print(f'{n1} is in range')
else:
    print(f'{n1} is out of range')