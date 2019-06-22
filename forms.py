from wtforms import Form, TextField, TextAreaField, validators, StringField, SubmitField

class MissionSearchForm(Form):
	'''
	Form to perform the search functionality
	in the /search route where one needs to
	type in the first and last name
	'''
	mission = TextField('Field', validators=[validators.DataRequired()])
