math = float(input("Enter your math marks:"))
if math < 0 or math > 100:
    print("Unrecognized value (Negative or Greater than 100)")
else:
    phy = float(input("Enter your english marks:"))
    if phy < 0 or phy > 100:
        print("Unrecognized value (Negative or Greater than 100)")
    else:
        geo = float(input("Enter your geography marks:"))
        if geo < 0 or geo > 100:
            print("Unrecognized value (Negative or Greater than 100)")
        else:
            chem = float(input("Enter your chemistry marks:"))
            if chem < 0 or chem > 100:
                print("Unrecognized value (Negative or Greater than 100)")
            else:
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
