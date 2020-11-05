

from flask import *
import json,urllib.request
import requests

app = Flask(__name__)
app.config['JSON_SORT_KEYS']=False
findic={}
##SOLUTION 1 COUNTRY REST API##
##TASK 1:-GET COUNTRY BY NAME##
@app.route('/country/name/<name>', methods=['GET'])
def freegeoip(name):
    obj="https://restcountries.eu/rest/v2/name/"+name.strip()+"?fullText=true"
    obj=requests.get(obj)
    obj=obj.json()
    findic["name"]=obj[0]["name"]
    findic["alpha2Code"]=obj[0]["alpha2Code"]
    findic["alpha3Code"]=obj[0]["alpha2Code"]
    findic["capital"]=obj[0]["capital"]
    findic["region"]=obj[0]["region"]
    findic["population"]=obj[0]["population"]
    findic["flag"]=obj[0]["flag"]
    findic["totalLanguages"]=count_dic(obj[0]["languages"])
    findic["totalCurrencies"]=count_dic(obj[0]["currencies"])
    return jsonify(findic)

#Task 2: Get country by Code
@app.route('/country/code/<code>', methods=['GET'])
def free(code):
  obj="https://restcountries.eu/rest/v2/alpha/"+code
  obj=requests.get(obj)
  obj=obj.json()
  findic["name"]=obj["name"]
  findic["alpha2Code"]=obj["alpha2Code"]
  findic["alpha3Code"]=obj["alpha3Code"]
  findic["capital"]=obj["capital"]
  findic["region"]=obj["region"]
  findic["population"]=obj["population"]
  findic["flag"]=obj["flag"]
  findic["totalLanguages"]=count_dic(obj["languages"])
  findic["totalCurencies"]=count_dic(obj["currencies"])
  findic["totalTimezones"]=len(obj["timezones"])
  return jsonify(findic)

def count_dic(dicto):
    count=0
    for i in dicto:
           count+=1
    return count

##TASK 3:-GET COUNTRY BY NAME##  

if __name__ == "__main__":
    app.run(debug=True)