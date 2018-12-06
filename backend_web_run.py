# -*- coding: utf-8 -*-
"""
Created on Sun Nov 25 14:25:39 2018

@author: Kawin-PC
"""

from flask import Flask,render_template,request
import webbrowser
from forms import Train_Form
from func import find_pathway


app=Flask(__name__)
app.secret_key='dev_key'

@app.route('/')
def index():
	fform=Train_Form()
	return render_template('main.html',form=fform)
	
@app.route('/show_answer/',methods=['GET','POST'])
def show_answer():
	fform=Train_Form()
	result=request.args
	starting_point=int(result['starting_point'])
	destination=int(result['destination'])
	ans=str(find_pathway(starting_point,destination))
	return render_template('main.html',ans=ans,form=fform)


if __name__=="__main__":
	webbrowser.open("http://127.0.0.1:8009")
	app.run(port=8009,debug=True)