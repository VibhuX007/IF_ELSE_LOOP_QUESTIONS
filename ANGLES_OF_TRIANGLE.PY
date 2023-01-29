#WRITE A PYTHON PROGRAM TO INPUT ALL ANGLES OF TRIANGLE AND CHECK WHETHER THE TRIANGLE IS VALID OR NOT

a = int(input("enter the first angle"))
b = int(input("enter the second angle"))
c = int(input("enter the third angle"))

if a+b+c == 180:
    print("triangle is valid")
else:
    print("triangle is not valid")