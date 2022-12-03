def Checkleap(year):
  if((year%400==0) or
     (year%100!=0) and
     (year%4==0)):
    print("GIVEN YEAR IS A LEAP YEAR"):
else:
    print("GIVEN YEAR IS NOT A LEAP YEAR")
    
year=int(input("ENTRE THE NUMBER:"))
Checkleap(year)
    
