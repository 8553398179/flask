# -*- coding: utf-8 -*-
"""
Created on Thu Oct 28 11:00:14 2021

@author: darshanRaghunath
"""
from flask import Flask,redirect, url_for, request

app = Flask(__name__)
 
# The route() function of the Flask class is a decorator,
# which tells the application which URL should call
# the associated function.
@app.route('/',methods =['GET'])
# ‘/’ URL is bound with hello_world() function.
def hello_world():
    jso = { "s1":
                {'h1':' 1',
                             '2':'h1'},
            "s2":{'h1': '2',
                              'h2': '3'}
                }
    
    return jso
@app.route('/success/<name>')
def hello_name(name):
   return 'Hello %s!' % name



@app.route('/login',methods = ['POST', 'GET'])
def login():
   if request.method == 'POST':
       print("Hello")
      
       user = request.form['nm']
       print(user)
       return("succes ")
      #return redirect(url_for('success',name = user))
   else:
      user = request.args.get('nm')
      return redirect(url_for('success',name = user))

# main driver function
if __name__ == '__main__':
 
    # run() method of Flask class runs the application
    # on the local development server.
    app.run()