#! /usr/bin/python


class entryExit(object):
    def __init__(self, f):
        print 'entry init enter'
        # save the input function as it's own class member function
        self.f = f
        print 'entry init exit'

    def __call__(self, *args):
        print "Entering", self.f.__name__
        r = self.f(*args)
        print "Exited", self.f.__name__
        return r

print 'decorator using'

@entryExit
def say_hello_to(a):
    print 'inside say_hello_to'
    return "hello " + a

print
print 'test start'
print
print say_hello_to('Mike')
print
print say_hello_to('Tim')
print
print say_hello_to('Jane')

'''
The method __call__ make the class entryExit become callable,

and decorator make hello function become:

say_hello_to = entryExit(say_hello_to)

'''
