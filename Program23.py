Number = int(input(" PLEASE ENTRE ANY NUMBER: "))

for i in range(2, Number + 1):
    if(Number % i == 0):
        isprime = 1
        for j in range(2, (i //2 + 1)):
            if(i % j == 0):
                isprime = 0
                break
            
        if (isprime == 1):
            print(" %d is a Prime Factor of a Given Number %d" %(i, Number))
