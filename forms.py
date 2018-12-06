from flask_wtf import Form
from wtforms import SelectField,SubmitField

from func import get_station

class Train_Form(Form):
	station=get_station()
	starting_point=SelectField('Starting Point : ',choices=station)
	destination=SelectField('Destination : ',choices=station)
	submit=SubmitField('send')