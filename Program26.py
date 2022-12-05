import math
a=int(input("ENTER FIRST SIDE : "))
b=int(input("ENTER SECOND SIDE: "))
c=int(input("ENTER THIRD SIDE: "))
s=(a+b+c)/2
area=math.sqrt(s*(s-a)*(s-b)*(s-c))
print("ARERA OF TRIANGLE IS : ",round(area,2))
