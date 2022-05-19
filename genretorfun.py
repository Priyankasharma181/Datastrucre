# def mygenerator():
#     print('First item')
#     yield 10

#     print('Second item')
#     yield 20

#     print('Last item')
#     yield 30
# a = mygenerator()
# for i in a:
#     print(i)



# num = int(input("enter the num"))
# def even(x):
#     if x%2==0:
#         yield x
#     yield "not even"    
# a = even(num)
# for i in a:
#     print(i)     

def a(h):
    yield  h+3
b = a(5)
for i in b:
    print(i) 
