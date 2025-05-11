x=99
def f1():
    x=88
    def f2():
        print(x)
    # f2()
    return f2
myresult = f1()
myresult()
# f1()