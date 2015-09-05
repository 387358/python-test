#! /usr/bin/python

'''
The first demo shows the variable scope, where the interger variable x in
function1 can not be changed by setX, because x is another local variable in the
setX function. However, if the variable in func1 is a mutable type like list or
dict, and it can be changed. Like the next example shows.
'''

def func1():
    x = 10
    def getX():
        print 'x =', x
        return

    def setX(a):
        x = a
        return

    return getX, setX

getX, setX = func1()

getX()
setX(20)
getX()


print
print '---------------'
print

'''
The following example shows the mutable dict variable stored in decorator
function are changed by return memorized function and function as the cached.
'''

def memorize(fib):
    print 'init stored dict'
    stored = {}
    def memorized(n):
        try:
            return stored[n]
        except KeyError:
            result = fib(n)
            stored[n] = result
            print 'stored:', stored
            return result

    return memorized

#fib = memorize(fib)
@memorize
def fib(n):
    if n in [0,1]:
        return n
    else:
        return fib(n-1) + fib(n-2)


print 'fib(6)'
print fib(6)
print
print 'fib(7)'
print fib(7)







