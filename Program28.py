rows = int(input("ENTER NUMBER OF ROW : "))

for i in range(rows):
    for j in range(i+1):
        print("*", end="")
    print("\n")
