#! /usr/bin/python


def who_say_hello(who):
    def who_say(f):
        def say(name):
            return who + ' say ' + f(name)
        return say
    return who_say

@who_say_hello('Tim')
def hello(name):
    return '"hello ' +  name + '"'

print hello('Tracy')



'''

The decorator function "who_say_hello" is a arguemented function, thus we need
use one more wrapper function "who_say_hello" to handle that. The "who_say" is an
original decorator function which take "hello" functino as arguement f, and "say"
is the original decorator return function. The "who_say_hello" take the decorator
arguements for the real decorator fucntion "who_say" to use.

'''




