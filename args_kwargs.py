#! /usr/bin/python

def my_func( *args, **kwargs):
    for arg in args:
        print 'arg:', arg

    for key, val in kwargs:
        print 'key:', key, 'val:', val


print "my_func('a1', 'a2', 'a3', k1='v1', k2='v2', k3='v3')"
my_func('a1', 'a2', 'a3', k1='v1', k2='v2', k3='v3')

print
print "l = ['a1', 'a2', 'a3']"
print "d = {'k1':'v1', 'k2':'v2', 'k3':'v3'}"
print
print 'my_func(l)'
l = ['a1', 'a2', 'a3']
d = {'k1':'v1', 'k2':'v2', 'k3':'v3'}
my_func(l)

print
print "my_func(*l, **d)"
my_func(*l, **d)
