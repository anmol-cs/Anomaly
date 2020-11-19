from flask import *
import json,urllib.request
import requests

app = Flask(__name__)
app.config['JSON_SORT_KEYS']=False
#SOLUTION 1: COUNTRY REST API
#TASK 1: GET COUNTRY BY NAME
@app.route('/country/name/<country_name>', methods=['GET'])
def nameSearch(country_name):
    obj='https://restcountries.eu/rest/v2/name/'+country_name
    obj=requests.get(obj)
    if obj:
        obj=obj.json()
        findic={}
        findic['name']=obj[0]['name']
        findic['alpha2Code']=obj[0]['alpha2Code']
        findic['alpha3Code']=obj[0]['alpha2Code']
        findic['capital']=obj[0]['capital']
        findic['region']=obj[0]['region']
        findic['population']=obj[0]['population']
        findic['flag']=obj[0]['flag']
        findic['totalLanguages']=count_dic(obj[0]['languages'])
        findic['totalCurrencies']=count_dic(obj[0]['currencies'])
        return jsonify(findic)
    else:
        return(err1)

#Task 2: Get country by Code
@app.route('/country/code/<country_code>', methods=['GET'])
def codeSearch(country_code):
    obj='https://restcountries.eu/rest/v2/alpha/'+country_code
    obj=requests.get(obj)
    if obj:
        obj=obj.json()
        findic={}
        findic['name']=obj['name']
        findic['alpha2Code']=obj['alpha2Code']
        findic['alpha3Code']=obj['alpha3Code']
        findic['capital']=obj['capital']
        findic['region']=obj['region']
        findic['population']=obj['population']
        findic['flag']=obj['flag']
        findic['totalLanguages']=count_dic(obj['languages'])
        findic['totalCurencies']=count_dic(obj['currencies'])
        findic['totalTimezones']=len(obj['timezones'])
        return jsonify(findic)
    else:
        return(err1)

#TASK 3: SEARCH COUNTRY 
@app.route('/country/search', methods=['GET'])
def Search():
    searchString=request.args['searchText']
    #check for name
    obj='https://restcountries.eu/rest/v2/name/'+searchString.strip()+'?fullText=true'
    obj=requests.get(obj)
    if obj:
        obj=obj.json()
        findic={}
        findic['name']=obj[0]['name']
        findic['capital']=obj[0]['capital']
        findic['population']=obj[0]['population']
        findic['flag']=obj[0]['flag']
        findic['totalLanguages']=count_dic(obj[0]['languages'])
        findic['totalCurrencies']=count_dic(obj[0]['currencies'])
        findic['totalTimezones']=len(obj[0]['timezones'])
        return jsonify(findic)
    else:#check for code
        obj='https://restcountries.eu/rest/v2/alpha/'+searchString
        obj=requests.get(obj)
        if obj:
            obj=obj.json()
            findic={}
            findic['name']=obj['name']
            findic['capital']=obj['capital']
            findic['population']=obj['population']
            findic['flag']=obj['flag']
            findic['totalLanguages']=count_dic(obj['languages'])
            findic['totalCurencies']=count_dic(obj['currencies'])
            findic['totalTimezones']=len(obj['timezones'])
            return jsonify(findic)
        else:#check for calling code               
            obj='https://restcountries.eu/rest/v2/callingcode/'+searchString
            obj=requests.get(obj)
            if obj:
                obj=obj.json()
                findic={}
                findic['name']=obj[0]['name']
                findic['capital']=obj[0]['capital']
                findic['population']=obj[0]['population']
                findic['flag']=obj[0]['flag']
                findic['totalLanguages']=count_dic(obj[0]['languages'])
                findic['totalCurencies']=count_dic(obj[0]['currencies'])
                findic['totalTimezones']=len(obj[0]['timezones'])
                return jsonify(findic)
            else:#check for capital 
                print('u reached in capital')              
                obj='https://restcountries.eu/rest/v2/capital/'+searchString
                obj=requests.get(obj)
                if obj:
                    obj=obj.json()
                    findic={}
                    findic['name']=obj[0]['name']
                    findic['capital']=obj[0]['capital']
                    findic['population']=obj[0]['population']
                    findic['flag']=obj[0]['flag']
                    findic['totalLanguages']=count_dic(obj[0]['languages'])
                    findic['totalCurencies']=count_dic(obj[0]['currencies'])
                    findic['totalTimezones']=len(obj[0]['timezones'])
                    return jsonify(findic)
                else:#ERROR
                    return(err1)

err1={'status':404,'message':'Country not found'}
def count_dic(dicto):
    count=0
    for i in dicto:
           count+=1
    return count

#SOLUTION 2: COVID-19
#TASK 4: Covid latest counts by COUNTRY NAME
@app.route('/covid/country/name/',methods=['GET'])
def covName():
    country_name=request.args['country_name']
    obj=''
err2={'status':404,'message':'no records found'}

if __name__ == '__main__':
    app.run(debug=True)