#PALINDROME NUMBER?
n = input()
r = n[::--1]
if n==r:
	print('Palindrome')
else:
	print('Not Palindrome')