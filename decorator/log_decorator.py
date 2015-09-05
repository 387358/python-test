#! /usr/bin/python


def logged1(func):
    def with_logging(*args, **kwargs):
        print 'func: ' + func.__name__ + ' was called'
        return func(*args, **kwargs)
    return with_logging

@logged1
def f(x):
    print 'into f(x)'
    return x*x
'''
above decorated func is equal to
def f(x):
    print 'into f(x)'
    return x*x
f = logged1(f)
'''
print 'f(3)'
print f(3)
print


def logged2(func):
    print 'func: ' + func.__name__ + ' was called'
    return func

@logged2
def f2(x):
    print 'into f2(x)'
    return x*x

print 'f2(3)'
print f2(3)
print f2(3)
print f2(3)
print

'''
decorator function was called when the module load, not when the function was
called. Thus you must warpper another function to return just like logged1, and
then the wrapper function will be called every time when the wrappered function
was called. Otherwise, the decorator will be called only once no matter how many
times the wrappered functino was calleds, just like logged2
'''

def logged3(func):
    print 'input func: ' + func.__name__
    def p(*args, **kwargs):
        print 'logged2 was called - args:', args, 'kwargs:', kwargs
    return p

@logged3
def f3(x):
    print 'into f3(x)'
    return x*x

print 'f3 call list'
print f3(3, 4, a=5)
print f3(3, 4, a=6)
print f3(3, 4, a=7)


'''
So, in the end, what the decorator acturally doing?

just override the original function as the decorator function and put the original
function as the arguement:

f3 = logged3(f3)

'''


