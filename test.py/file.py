import random
def roll():
    min=1
    max=6 
   
    x=int(input("choose 1-6 u have 2 chance:"))
    roll=random.randint(min,max)
    if roll==x:
        print("correct")
    else:
       print(f'"not correct :"{roll} "not"{x}')

    y=int(input("choose 1-6 u have 1 chance:"))
    if roll==y:
        print("correct")
    else:
         print(f'"not correct again:"{roll} "is not"{y}') 
    return roll
       
val=roll()
print(f'rolldie:{val}')