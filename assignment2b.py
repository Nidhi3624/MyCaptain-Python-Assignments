#python program to print all positive numbers in a range

list=[]
list2=[]

n=int(input("enter the number of elements in the list:"))

for i in range(n):
    x=int(input("enter an element:"))
    list.append(x)
print("input=",list)

for j in range(n):
    if list[j]>0:
        list2.append(list[j])
print("output=",list2)

