#!/usr/bin/env python
# -*- coding: utf8 -*-


from flask import Flask,request,redirect,render_template,session

app=Flask(__name__)
app.config["SECRET_KEY"] = "test"



@app.route('/login/check')
def login_check():
    name=request.values.get('name')
    pwd=request.values.get('pwd')
    session['logined']=True
    if name =='tom' and pwd == '123':
        return redirect('/email/look')
    else:
        return redirect('/')

@app.route('/email/look')
def email_show():
    logined=session.get('logined')
    if logined:
        return 'this is index page of email!'
    else:
        return redirect('/')

@app.route('/')
def login():
    return render_template('login.html')

if __name__ == '__main__':
    app.run(debug=True)
