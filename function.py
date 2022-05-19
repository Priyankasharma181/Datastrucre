# key word
# def sum(a,b,c):
#     print(a,b,c)
# sum(b=89,a=21,c=45)
# # arbitary keyword
# def sum(*a):
#     print(a)
# sum(5,7,8,9)    
# # postional 
# def sum(a):
#     print(a)
# sum(5)    
# # default
# def sum(s=9):
#     print(s)
# sum(5)    


def fac(a):
    if a==1:
        return 1
    return a*(fac(a-1))
print(fac(6))      
