# code to create a function called most_frequent that takes a string and prints the letters in decreasing order of frequency Using dictionaries.

def most_frequent():
    dict={}
    s=input("enter a string:")

    for i in range(len(s)):
        a=s[i]
        count=0
        for j in range(len(s)):
            if s[j]==a:
                count=count+1
        dict[a]=count

    values=list(dict.values())
    keys=list(dict.keys())

    for m in range(len(s)):
        for n in range(len(values)):
            if m==values[n]:
                print(keys[n],":",values[n])

most_frequent()