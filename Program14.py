number=int(input(" ENTRE ANY NUMBER "))

if number>1:
  for i in range(2,number):
    if(number%i)==0:
      print(number," IS NOT A PRIME NUMBER ")
    break
else:
  print(number," IS A PRIME NUMBER ")

else:
  print(number," IS NOT A PRIME NUMBER ") 
