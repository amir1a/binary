arr=list(range(1,100))
def binary_search(arr_list,target):
       arr_list.sort()
       print(arr_list)
       low=0
       high=len(arr_list)-1
       counter=1
       while high>=low:
              print(f'{counter} try.')
              counter=+1
              mid=(high+low)//2
              if arr_list[mid]==target:
                    print(f'Target:{target} found.in index {mid} ')
                    return
              
              elif arr_list[mid]>target:
                  
                    high=mid-1
                    
              else:
                   
                    low=mid+1
       print(f'Target:{target} not found in arrar.')       
   
binary_search([5,46,34,45,2,4,6,3,12,32,16],34)
