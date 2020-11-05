

from flask import *
import json,urllib.request
import requests

app = Flask(__name__)
app.config['JSON_SORT_KEYS']=False
##SOLUTION 1 COUNTRY REST API##
##TASK 1:-GET COUNTRY BY NAME##
@app.route('/country/name/<country_name>', methods=['GET'])
def freegeoip(country_name):
    url="https://restcountries.eu/rest/v2/name/"+country_name.strip()+"?fullText=true"
    url_request=requests.get(url)
    json_object=url_request.json()
    findic={}
    findic["name"]=json_object[0]["name"]
    findic["alpha2Code"]=json_object[0]["alpha2Code"]
    findic["alpha3Code"]=json_object[0]["alpha2Code"]
    findic["capital"]=json_object[0]["capital"]
    findic["region"]=json_object[0]["region"]
    findic["population"]=json_object[0]["population"]
    findic["flag"]=json_object[0]["flag"]
    findic["totalLanguages"]=count_dic(json_object[0]["languages"])
    findic["totalCurrencies"]=count_dic(json_object[0]["currencies"])
    print(findic)
    return jsonify(findic)

#Task 2: Get country by Code
@app.route('/country/code/<code>', methods=['GET'])
def free(code):
  url="https://restcountries.eu/rest/v2/alpha/"+code
  print(url)
  url_request=requests.get(url)
  json_object=url_request.json()
  findic={}
  findic["name"]=json_object["name"]
  findic["alpha2Code"]=json_object["alpha2Code"]
  findic["alpha3Code"]=json_object["alpha3Code"]
  findic["capital"]=json_object["capital"]
  findic["region"]=json_object["region"]
  findic["population"]=json_object["population"]
  findic["flag"]=json_object["flag"]
  findic["totalLanguages"]=count_dic(json_object["languages"])
  findic["totalCurencies"]=count_dic(json_object["currencies"])
  findic["totalTimezones"]=len(json_object["timezones"])
  return jsonify(findic)

def count_dic(dicto):
    count=0
    for i in dicto:
           count+=1
    return count

##TASK 3:-GET COUNTRY BY NAME##  

if __name__ == "__main__":
    app.run(debug=True)