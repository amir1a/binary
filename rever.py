import re
def revers(string):
    rev=""
    for i in range(len(string)-1,-1,-1) :
         rev=rev+string[i]
    for i in range(len(rev)-1,-1,-1) :    
     if rev[i] =="a":
             rev=re.sub("a","1",rev)
     elif rev[i]=="e":   
             rev=re.sub("e","2",rev)
     elif rev[i]=="i":  
               rev=re.sub("i","3",rev)
     elif rev[i]=="o":
             rev=re.sub("o","4",rev)
     elif rev[i]=="u":   
             rev=re.sub("a","5",rev)
     else: pass         
 
    print(f'the encrypted string:{rev}') 
    return rev


def dec(be):
    for i in range(len(be)-1,-1,-1) :
         be=string[i] + be
    for i in range(len(be)-1,-1,-1) :    
     if be[i] =="1":
             be=re.sub("1","a",be)
     elif be[i]=="2":   
             be=re.sub("2","e",be)
     elif be[i]=="3":  
               be=re.sub("3","i",be)
     elif be[i]=="4":
             be=re.sub("4","o",be)
     elif be[i]=="5":   
             be=re.sub("5","u",be)
     else: pass     
   
    print(f'the decrypted string:{be}')     
string=input("enter string :")
be=revers(string)
dec(be)