#!/usr/bin/env python


def set_color(func):
    def set_red(*args):
        return '\033[31;1m%s\033[0m' % func(*args)
    return set_red

@set_color
def welcome(word):
    return 'welcome to %s' % word

@set_color
def say_hi():
    return 'How are you?'

if __name__ == '__main__':
    print welcome('China')
    print welcome('Tedu')
    print say_hi()