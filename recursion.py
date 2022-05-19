# def sum(n):
#     if n ==1:
#         return 1
#     return n+(sum(n-1))    
# print(sum(10))  

def fab(num):
    if num ==0 or num == 1:
        return num
    return fab(num-1)+fab(num-2)    
print(fab(6))    


