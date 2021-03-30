def cos(x):
    print(x)

cos(2)

def zewnetrzna(a):
    def wewnetrzna():
        print(a)
    wewnetrzna()

zewnetrzna(3)

def operator(s):
    def plus(a,b):
        return a+b
    def minus(a,b):
        return a-b
    if s=="+":
        return plus
    elif s=="-":
        return minus
o=operator("+")
print(o)
print(o(2,3))

def add(n):
    def add_imple(x):
        return n+x
    return add_imple
print(add(1)(2))

def mr(fn):
    def jakkolwiek(s):
        s="mr {}".format(s)
        return fn(s)
    return jakkolwiek
@mr
def hello(s):
    return "hello {}".format(s)

print(hello("Darek"))