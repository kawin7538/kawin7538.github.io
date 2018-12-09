# -*- coding: utf-8 -*-
"""
Created on Sun Nov 25 14:25:39 2018

@author: Kawin-PC
"""

from flask import Flask,render_template,request,redirect
import webbrowser
from forms import Train_Form
from func import find_pathway
from flask_wtf.csrf import CSRFProtect


app=Flask(__name__)
app.config['SECRET_KEY']='ajskdgajsldhfuasfflagw7gf7awg'
csrf=CSRFProtect(app)

@app.route('/index')
def index(Errorror="",ans=""):
	fform=Train_Form()
	header="Main Page Of Train"
	return render_template('main.html',ans=ans,form=fform,header=header,Errorror=Errorror)
	
@app.route('/show_answer/',methods=['POST','GET'])
def show_answer():
	result=request.args
	starting_point=int(result['starting_point'])
	destination=int(result['destination'])
	ans=find_pathway(starting_point,destination)
	fform=Train_Form(starting_point=str(starting_point),destination=str(destination))
	if ans==3:
		return index(Errorror="You should choose difference station")
	else:
		ans=[i.split('\n') for i in ans]	
		header = 'Main Page Of Train'
	return render_template('main.html',ans=ans,form=fform,header=header)
	

if __name__=="__main__":
	webbrowser.open("http://127.0.0.1:8009/index")
	app.run(port=8009,debug=True)