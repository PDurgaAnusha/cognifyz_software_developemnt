def number_pyramid(rows):
    print("Number Pyramid Pattern")
    for i in range(1, rows + 1): 
        print(" " * (rows - i), end="")
        for j in range(1, i + 1):
            print(j, end="")
        for j in range(i - 1, 0, -1):
            print(j, end="")
        print()  # Move to the next line
rows = int(input("Enter the number of rows for the pyramid: "))
number_pyramid(rows)
