math = 100
eng = 90
geo = 85
chem = 65

Total = math + eng + geo + chem
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