#! /usr/bin/python


def who_say_hello(who):
    def who_say(f):
        def say(name):
            return who + ' say ' + f(name)
        return say
    return who_say

# hello = who_say_hello(who)(hello)
@who_say_hello('John')
def hello(name):
    return '"hello ' +  name + '"'

print hello('Jim')



'''

The decorator function "who_say_hello" is a arguemented function, thus we need
use one more wrapper function "who_say_hello" to handle that. The "who_say" is an
original decorator function which take "hello" functino as arguement f, and "say"
is the original decorator return function. The "who_say_hello" take the decorator
arguements for the real decorator fucntion "who_say" to use.

'''

'''
Or use the decorator class object is more clear for saperator init decorator and
call the decorated function
'''

print '-------------------------'

class who_say_hello2(object):
    def __init__(self, who):
        self.who = who

    def __call__(self, f):
        def say(name):
            return self.who + ' say ' + f(name)
        return say

#hello2 = who_say_hello2(who)(hello2)
@who_say_hello2('Tim')
def hello2(name):
    return '"hello ' +  name + '"'

print hello2('Tracy')



