
math=float(input("enter your math marks"))
phy=float(input("enter your english marks"))
geo=float(input("enter your geogrphy marks"))
chem=float(input("enter your chemistry marks"))


Total = math + phy + geo + chem
Avg = Total/4

if Avg < 0:
    print("Unrecognized average (Negative)")

elif Avg > 100:
    print("Unrecognized average (Greater than 100)")
elif Avg >= 71:
        print("A")
elif Avg >= 51:
        print("B")
elif Avg >= 31:
        print("C")
else:
        print("D")