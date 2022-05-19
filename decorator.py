def fun():
    def fun2():
        print("priyanka")
    return fun2
n = fun()
n()


def fun():
    print("priyanka")
fun2 = fun
del fun
fun2()
