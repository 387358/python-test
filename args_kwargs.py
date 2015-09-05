#! /usr/bin/python

def my_func( *args, **kwargs):
    for arg in args:
        print 'arg:', arg

    for key, val in kwargs:
        print 'key:', key, 'val:', val


my_func('a1', 'a2', 'a3', k1='v1', k2='v2', k3='v3')
