from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')

def index():
    title = 'EDC Data Lineage'
    return render_template("index.html", title=title)


@app.route('/about')

def about():
    names = ['John','Frank','Mary','Elsa']
    return render_template("about.html", names=names)
