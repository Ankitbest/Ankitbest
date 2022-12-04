a = int(input('ENTER FIRST NUMBER : '))
b = int(input('ENTER SECOND NUMBER : '))
c = int(input('ENTER THIRD NUMBER : '))

smallest = 0

if a < b and a < c :
    smallest = a
if b < a and b < c :
    smallest = b
if c < a and c < b :
    smallest = c

print(smallest, "IS THE SMALLEST OF THREE NUMBER.")
