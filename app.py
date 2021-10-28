from flask import Flask, render_template
from waitress import serve
app = Flask(__name__)

@app.route('/')

def index():
    title = 'EDC Data Lineage'
    return render_template("index.html", title=title)


@app.route('/about')

def about():
    names = ['John','Frank','Mary','Elsa']
    return render_template("about.html", names=names)

if __name__ == '__main__':
    serve(app, host='0.0.0.0', port=8080)
