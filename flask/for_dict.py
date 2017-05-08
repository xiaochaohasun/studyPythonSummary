#!/usr/bin/env python
# -*- coding: utf8 -*-


from flask import Flask,request,redirect,render_template

app=Flask(__name__)


@app.route('/')
def for_dict():
    data=[
        {'name':'hasun','age':40},
        {'name':'kevin','age':20},
        {'name':'ailce','age':30},
    ]
    return render_template('for_dict.html',data=data)

if __name__ == '__main__':
    app.run(debug=True)
