n=int(input("Enter any number"))
sum=0
temp=n
while temp>0:
    digit=temp % 10
    sum+=digit**3
    temp//=10

if n==sum:
    print("The number is an amstrong number")
else:
    print("Not an amstrong number")
