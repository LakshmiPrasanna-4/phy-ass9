# Write a program to print given number is a prime number or not.

n=int(input())
c=0
for i in range(1,n+1,1):
    if n%i==0:
        c=c+1
if c==2:
    print('yes')
else:
    print('no')
