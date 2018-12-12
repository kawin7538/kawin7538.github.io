# -*- coding: utf-8 -*-
"""
Created on Sun Nov 25 14:25:39 2018

@author: Kawin-PC
"""
from flask import Flask,render_template,request,redirect,jsonify
import webbrowser
from forms import Train_Form
from func import find_pathway
from flask_wtf.csrf import CSRFProtect

app=Flask(__name__)
app.config['SECRET_KEY']='ajskdgajsldhfuasfflagw7gf7awg'
csrf=CSRFProtect(app)

@app.route('/')
def main(Err="",starting_point='',destination=''):
	form=Train_Form(starting_point=starting_point,destination=destination)
	return render_template('main_beautiful.html',form=form,Err=Err)
	
@app.route('/show_answer',methods=['POST'])
def show_answer():
	starting_point=request.form['starting_point']
	destination=request.form['destination']
	result=find_pathway(int(starting_point),int(destination))
	if result==3:
		return main(Err='Your starting point and destination should be different',starting_point=starting_point,destination=destination)
	else:
		result=[i.split('\n') for i in result]
		other_offer=[]
		if len(result)==1:
			other_offer=''
		else:
			other_offer=result[1:]
		return render_template('show_answer.html',best_offer=result[0],other_offer=other_offer)
	
	

if __name__=="__main__":
	webbrowser.open("http://127.0.0.1:8009/")
	app.run(port=8009)