def get_valid_input(prompt):
    while True:
        value = float(input(prompt))
        if 0 <= value <= 100:
            return value
        else:
            print("Invalid input. Please enter a value between 0 and 100.")

math = get_valid_input("Enter your math marks: ")
phy = get_valid_input("Enter your english marks: ")
geo = get_valid_input("Enter your geography marks: ")
chem = get_valid_input("Enter your chemistry marks: ")

Total = math + phy + geo + chem
Avg = Total / 4

if Avg >= 71:
    print("A")
elif Avg >= 51:
    print("B")
elif Avg >= 31:
    print("C")
else:
    print("D")
