from flask import Flask, request, redirect
import twilio.twiml

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def hello_monkey():
	#responds to text message with a static response
	resp = twilio.twiml.Response()
	resp.message("Click on this link to donate to Project Homeless Connect!")
	return str(resp)


if __name__=="__main__":
	app.run(debug=True)