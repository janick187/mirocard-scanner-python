import json
from flask import Flask, request, Response, render_template


current_temperature = 0
current_humditiy = 0

app = Flask(__name__)

@app.route('/temperature', methods = ['GET'])
def getTemperature():
    
    # read current temperature from file
    f = open("values.txt", "r")
    lines = f.readlines()
    for line in lines:
        print(line)
    
    response_json = {
        'temperature':lines[0].strip().split(": ")[1]
        }

    resp = Response(json.dumps(response_json))
    return resp

@app.route('/humidity', methods = ['GET'])
def getHumidity():
    
    # read current temperature from file
    f = open("values.txt", "r")
    lines = f.readlines()
    for line in lines:
        print(line)
    
    response_json = {
        'humidity':lines[1].strip().split(": ")[1]
        }

    resp = Response(json.dumps(response_json))
    return resp
