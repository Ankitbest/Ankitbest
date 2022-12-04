a = int(input('ENTRE THE FIRST NUMBER : '))
b = int(input('ENTRE THE SECOND NUMBER : '))
c = int(input('ENTRE THE THIRD NUMBER: '))

largest = 0

if a > b and a > c:
    largest = a
if b > a and b > c:
    largest = b
if c > a and c > b:
    largest = c

print(largest, "IS THE LARGEST NUMBER OF THREE NUMBERS .")
