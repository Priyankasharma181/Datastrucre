class stack:
    def __init__(self):        #it is initlizer (__init__)
        self.name = []
    def push(self, a):
        self.name.append(a)
        return a
    def pop(self):
        return self.name.pop() 
x = stack()
x.push(12)
x.push(23)
x.push(24)
print(x.pop())
print(x.pop())
