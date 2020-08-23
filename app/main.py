from flask import Flask, redirect, render_template, request

app = Flask(__name__)
@app.route("/")
def landing_page():
    return render_template ("index.html")

@app.route("/static/images/title.jpg")
def landing_page():
    return render_template ("/static/images/title.jpg")
