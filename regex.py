import re

text="subsicribe gj tube"
t=re.findall("be",text)
print(t)  
v=re.search("\s",text)
print("the first space ",v.start())
g=re.split("\s",text)
print(g)
t=re.sub("tube","tech",text)
print(t)
sum=0
for i in range(0,101,5):
    sum=sum+i
    print(sum)