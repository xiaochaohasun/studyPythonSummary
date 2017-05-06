#!/usr/bin/env python
# -*- coding: utf8 -*-


from flask import Flask

app=Flask(__name__)

@app.route('/')
@app.route('/abc')
def hello():
    print hello
    return "hello,world!"

if __name__ == '__main__':
    app.run()