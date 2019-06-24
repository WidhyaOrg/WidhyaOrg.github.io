from flask import Flask, render_template, flash, request, redirect, url_for, session
import sendgrid
import os
from forms import *

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

@app.route("/", methods=['GET','POST'])
def index():
	return redirect(url_for('browse_missions'))

@app.route("/<string:username>", methods=['GET', 'POST'])
def dashboard(username):
	print(username)
	return render_template("dashboard.html")

@app.route("/browse-missions", methods=['GET', 'POST'])
def browse_missions():
	form = MissionSearchForm(request.form)	#Gets mission form
	if(request.method == 'POST'):	#If form submitted
		#print(form.validate())
		if(form.validate()):
			print("\"" + request.form['mission']+ "\"")	#Gives value entered in search field
			return render_template("browse_missions.html", form=form)
	return render_template("browse_missions.html", form=form)

'''@app.errorhandler(404)
def not_found(e):
	return render_template("404.html")
'''

@app.route("/solvemicrotask",methods=['GET','POST'])
def main():
	return render_template("solvemicrotask.html")
@app.route("/companydashboard",methods=['GET','POST'])
def companydashboard():
	return render_template("companydashboard.html")
@app.route("/uploadmicrotask",methods=['GET','POST'])
def uploadmicrotask():
	return render_template("uploadmicrotask.html")
@app.route("/opportunity",methods=['GET','POST'])
def opportunity():
	return render_template("opportunity.html")
@app.errorhandler(500)
def application_error(e):
	return 'Sorry, unexpected error: {}'.format(e), 500

if(__name__ == "__main__"):
	app.run(debug=True)
