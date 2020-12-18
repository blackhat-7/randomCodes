d = {
    0: 'Zero',
    1: 'One',
    2: 'Two',
    3: 'Three',
    4: 'Four',
    5: 'Five',
    6: 'Six',
    7: 'Seven',
    8: 'Eight',
    9: 'Nine'
}

number = int(input('Enter your number:'))

lst = []
while number != 0:
    last_digit = number % 10
    lst += [d[int(last_digit)]]
    number = int(number/10)
lst = lst[::-1]

print(lst)
print(' '.join(lst))


