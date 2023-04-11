#program to print area of a circle

r=float(input("Enter the radius of the circle:"))
area= (22/7)*r*r
print("area of the the circle with radius", r, "is", area)


#program to accept a filename from the user and print extension of the file

file=input("Enter the filename:")
n=len(file)
for i in range(n):
    if file[i]==".":
        ext=file[i:n+1]
    
if ext==".py":
    print("Extension of the file is python")
elif ext==".html":
    print("Extension of the file is html")
elif ext==".pdf":
    print("Extension of the file is pdf")
elif ext==".doc":
    print("Extension of the file is document")
else:
    print("Try Again...")

