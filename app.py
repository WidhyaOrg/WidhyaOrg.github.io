from flask import Flask, render_template, flash, request, redirect, url_for, session
from wtforms import Form, TextField, TextAreaField, validators, StringField, SubmitField
import sendgrid

users = 0

class ContactForm(Form):
	name = TextField('Full Name', validators=[validators.DataRequired()], render_kw={"placeholder": "Name"})
	email = TextField('Email ID', validators=[validators.DataRequired()], render_kw={"placeholder": "Email"} )
	phone = TextField('Phone Number', validators=[validators.DataRequired()], render_kw={"placeholder": "Phone Number"})
	foi = TextField('Field Of Interest', validators=[validators.DataRequired()], render_kw={"placeholder": "Field Of Interest"})

def send_mail(users, name, email, ph_num, field):
	sg = sendgrid.SendGridAPIClient(apikey = os.environ.get("SG_API_KEY"))
	from_email = sendgrid.helpers.mail.Email("rahulkumaran313@gmail.com", name="Rahul Arulkumaran")
	#print(subject_given.split("-")[0])
	to_email = sendgrid.helpers.mail.Email("widhya.contacts@gmail.com")
	#print(to_email)
	subject = str(users) + " User's Contact Details Bruh"
	content = sendgrid.helpers.mail.Content("text/html", "Hey Widhya, I hope this doesn't get into spam lol! xD <br>Wrote the above thing to escape spam. xD Hope it works dude! <br> The details are mentioned below!<br><br>Request: %s <br>Name of the person is <b>%s</b> <br>Email address is <b>%s</b> <br>Number is <b>%s</b> <br>Field Of Interest is <b>%s</b> <br>"%(users, name, email, ph_num, field))
	mail = sendgrid.helpers.mail.Mail(from_email, subject, to_email, content)
	response = sg.client.mail.send.post(request_body=mail.get())
	return response

DEBUG = True
app = Flask(__name__)	#initialising flask
app.config.from_object(__name__)	#configuring flask
app.config['SECRET_KEY'] = '7d441f27d441f27567d441f2b6176a'

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def index():
	form = ContactForm(request.form)
	if(request.method == 'POST'):
		if(form.validate()):
			global users
			users += 1
			response = send_mail(users, request.form['name'],request.form['email'],request.form['phone'],request.form['foi'])
	return render_template("index.html", form=form)


'''@app.errorhandler(404)
def not_found(e):
	return render_template("404.html")


@app.errorhandler(500)
def application_error(e):
	return 'Sorry, unexpected error: {}'.format(e), 500'''

if(__name__ == "__main__"):
	app.run(debug=True)
