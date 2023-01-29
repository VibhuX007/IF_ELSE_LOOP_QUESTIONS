#ENTER A NUMBER AND CHECK WHETHER IT IS PERFECT OR NOT?
n = int(input("enter a number:"))
s = 1
for i in range(2,n):
    s += i if n%i==0 else 0
if n==s:
    print('perfect no.')
else:
    print('not a perfect no.')