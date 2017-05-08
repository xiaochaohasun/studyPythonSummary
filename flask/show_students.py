#!/usr/bin/env python
# -*- coding: utf8 -*-


from flask import Flask,request,redirect,render_template
import mysql_driver as mydr

app=Flask(__name__)


@app.route('/')
def show_students():
    db=mydr.getDB()
    n,data=db.query("select * from student")
    return render_template('show_students.html',data=data)

if __name__ == '__main__':
    app.run(debug=True)