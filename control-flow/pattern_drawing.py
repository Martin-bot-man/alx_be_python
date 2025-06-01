x = int(input("Enter the size of the pattern: "))

for i in range (1, x+1):
    for j in range(x):
        print("*", end="", )
    print("", end="")  

    print("")  # This line seems to be intended to create a new line, but it should be just print() for a new line.


