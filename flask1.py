from flask import Flask, redirect, url_for

app = Flask(__name__)
a = False

@app.route("/")
def home():
	return "Hello! this is the main page <H1> HELLO <H1>"

@app.route("/<name>")
def user(name):
	return f"Hello{name}!"

@app.route("/admin")
def admin():
	if a:
	return redirect(url_for("home"))

if __name__ == "__main__":
	app.run()