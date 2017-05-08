#!/usr/bin/env python
# -*- coding: utf8 -*-


from flask import Flask,request,redirect,render_template

app=Flask(__name__)

@app.route('/')
def score():
    name=request.values.get('name')
    age=request.values.get('age')
    return render_template("userinfo.html",name=name,age=age)

if __name__ == '__main__':
    app.run(debug=True)