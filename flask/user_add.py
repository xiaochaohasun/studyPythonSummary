#!/usr/bin/env python
# -*- coding: utf8 -*-


from flask import Flask

app=Flask(__name__)



# @app.route('/useradd/<username>%<age>')
# @app.route('/useradd/<username>&<age>')
@app.route('/useradd/<username>/<age>')
def user_add(username,age):
    result='username=%s,age=%s' %(username,age)
    return result

if __name__ == '__main__':
    app.run()