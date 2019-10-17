from flask import Flask, render_template, flash, request, redirect, url_for, session, send_file
from wtforms import Form, TextField, TextAreaField, validators, StringField, SubmitField
import sendgrid
import os

users = 0

class ContactForm(Form):
	name = TextField('Full Name', validators=[validators.DataRequired()], render_kw={"placeholder": "Name"})
	email = TextField('Email ID', validators=[validators.DataRequired()], render_kw={"placeholder": "Email"} )
	phone = TextField('Phone Number', validators=[validators.DataRequired()], render_kw={"placeholder": "Phone Number"})
	foi = TextField('Field Of Interest', validators=[validators.DataRequired()], render_kw={"placeholder": "Field Of Interest"})

def send_mail(users, name, email, ph_num, field):
	sg = sendgrid.SendGridAPIClient(apikey = os.environ.get("SG_API_KEY"))
	from_email = sendgrid.helpers.mail.Email("widhya.org@gmail.com", name="Widhya Org")
	#print(subject_given.split("-")[0])
	to_email = sendgrid.helpers.mail.Email("rahuldravid313@gmail.com")
	#print(to_email)
	subject = "Subscribers List "
	mail_content = "Name : <b>%s</b> <br>Email ID : <b>%s</b> <br>Number : <b>%s</b> <br>Field Of Interest : <b>%s</b> <br>"%(name, email, ph_num, field)
	content = sendgrid.helpers.mail.Content("text/html", "<html><body><p>Thanks for actually using this particular thingy. I hope you're doing good! Thank those who actually agreed to use this particular website.</p> <br> <pre>%s</pre></body></html>"%(mail_content))
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
			return redirect(url_for("index"))
	return render_template("index.html", form=form)


@app.route("/rahul", methods=['GET', 'POST'])
def rahul():
	return send_file("docs/Rahul_VisitingCard.pdf")

@app.route("/rishabh", methods=['GET', 'POST'])
def rishabh():
	return send_file("docs/Rishabh_VisitingCard.pdf")

'''@app.errorhandler(404)
def not_found(e):
	return render_template("404.html")
'''

@app.errorhandler(500)
def application_error(e):
	return 'Sorry, unexpected error: {}'.format(e), 500

if(__name__ == "__main__"):
	app.run(debug=True)
