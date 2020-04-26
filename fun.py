def foo(a):
    print("I am calling foo ==>", a)

def bar(a):
    print("I am cxalling bar ==>", a)

def Conv2D(b):
    if b<5:
        return foo
    else:
         return bar

Conv2D(5)(45)