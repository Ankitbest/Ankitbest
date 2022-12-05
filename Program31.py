Rows = int(input("GIVE THE NUMBER OF ROW :"))  
Columns = int(input("GIVE THE NUMBER OF. COLOUMN:"))  
  
example_matrix = []  
print("Please give the entries row-wise:")  
   
for _ in range(Rows): 
    r = []  
    for __ in range(Columns):  
        r.append(int(input()))  
    example_matrix.append(r)  
for _ in range(Rows):  
    for __ in range(Columns):  
        print(example_matrix[_][__], end=" ")  
    print()  
