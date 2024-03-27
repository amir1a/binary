name = "amir birhanu"
x = len(name)-1
y=''
z=''
newname = ""
while x>=0:
    if name[x]!= " ":
        z += name[x]
    else:
        f=len(z)
        while f>=0:
            y +=z[f]
    y += name[x]
    x -=1
print(y)
