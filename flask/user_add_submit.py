#!/usr/bin/env python
# -*- coding: utf8 -*-


from flask import Flask,request

app=Flask(__name__)



# @app.route('/useradd/<username>%<age>')
# @app.route('/useradd/<username>&<age>')
@app.route('/useradd',methods=['POST','GET'])
def user_add():
    #ALL
    username=request.values.get('username')
    age=request.values.get('age')
    # #POST
    # username=request.form.get('username')
    # age=request.form.get('age')
    # #GET
    # username=request.args.get('username')
    # age=request.args.get('age')
    result='http get: username=%s,age=%s' %(username,age)
    return result

if __name__ == '__main__':
    app.run()