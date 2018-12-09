from flask_wtf import FlaskForm
from wtforms import SelectField,SubmitField

from func import get_station

class Train_Form(FlaskForm):
	station=get_station()
	starting_point=SelectField('Starting Point : ',choices=station)
	destination=SelectField('Destination : ',choices=station)