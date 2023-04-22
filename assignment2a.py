#python program to print fibonacci series upto n terms
n=int(input("enter a number:"))
f1=0
f2=1
for i in range(n):
    print(f1, end=" " )
    temp=f1+f2
    f2=f1
    f1=temp

