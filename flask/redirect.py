#!/usr/bin/env python
# -*- coding: utf8 -*-


from flask import Flask,request,redirect

app=Flask(__name__)

@app.route('/')
def score():
    return "<font color=red size=100>hello</font>"

@app.route('/score')
def score():
    score=request.values.get("score")
    n=int(score)

    if n<50:
        return "<font color=red size=100>Not Normal,hard study!</font>"
    elif n>60 and n<80:
        return "<font color=yellow size=100>Normal</font>"
    else:
        return redirect("/static/good.html")
    return faild