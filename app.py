from flask import Flask, render_template, request
from waitress import serve
import requests
app = Flask(__name__)


def lineage(seed):
    payload = {'association':'core.DirectionalDataFlow','depth':0,'direction':'BOTH','includeRefObjects':'false','includeTerms':'false','removeDuplicateAggregateLinks':'true','seed':seed}

    response = requests.get("https://inf-app1.edc-001.preprod.us-west-2.aws.redhat.com:9086/access/2/catalog/data/relationships", params=payload,verify=False, auth=('Administrator', 'Informatica'))

    lng = response.json()

    lst = set()

    for dict in lng['items'] :

        lst.add(dict['inId'])
    return lst



@app.route('/')

def index():
    title = 'EDC Data Lineage'
    return render_template("index.html", title=title)

@app.route('/submit' , methods = ['POST'])

def submit():


    schema_name = request.form.get("schema_name")
    table_name = request.form.get("table_name")
    column_name = request.form.get("column_name")

    seed = 'SFDC_Sales_Stage://'+schema_name+'/'+table_name+'/'+column_name
    names = list(lineage(seed))
    names.sort()

    return render_template("submit.html", names=names)

if __name__ == '__main__':
    serve(app, host='0.0.0.0', port=8080)
