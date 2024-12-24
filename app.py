from flask import Flask, request, jsonify
import random
import math
import queue
import threading
from threading import Timer
import time
import requests

app = Flask(__name__)
n=10
av_computers=[True]*n
requestQUEUE=[]
submissions = 0
avgQueueLength = 0
requestsStartTimes = {} # port:starttiTime
avgDelayTime = 0
@app.route('/', methods=['GET'])
def home():
    return jsonify({'message': 'Hello, World!'})

@app.route('/hello', methods=['GET'])
def hello():
    return jsonify({'message': 'Hello, World!'})

@app.route('/simulate', methods=['GET'])
def simulate():
    global submissions, avgQueueLength
    if request.method == 'GET':
        # send to another flask server
        taken=False
        submissions+=1
        avgQueueLength += len(requestQUEUE)
        for i in range(n):

            if av_computers[i]:
                print(f"Computer {i} is available")
                taken=True
                av_computers[i]=False
                url = f'http://localhost:{5000+i+1}/api/device-{5000+i+1}/recieved'
                data = {'message': 'data sent'}
                requestsStartTimes[i+5001] = int(time.time())
                response = requests.post(url, json=data,
                                         headers={'Content-Type': 'application/json'})
               
                return response.json()
        if not taken:
            print("All computers are busy")
            requestQUEUE.append(int(time.time()))
            print(requestQUEUE,"requestQUEUE")
            return jsonify({'message': 'Simulation not started!'})
        

        
   
@app.route('/api/device-5000/recieved', methods=['POST'])
def recieved():
    if request.method == 'POST':
        data = request.json
        global requestQUEUE, avgDelayTime
        avgDelayTime += (int(time.time()) - requestsStartTimes[5001+int(data['computerNumber'])])
        print("Waiting time for request from port ", 5001+int(data['computerNumber']), " ", int(time.time()) - requestsStartTimes[5001+int(data['computerNumber'])])
        
        print(requestQUEUE,"requestQUEUE33")
        if len(requestQUEUE)>0:
           requestsStartTimes[5001+int(data['computerNumber'])] = requestQUEUE[0]
           requestQUEUE= requestQUEUE[1:]
           requests.post(f"http://localhost:{5001+int(data['computerNumber'])}/api/device-{5001+int(data['computerNumber'])}/recieved",json={
                'message': 'data sent'
           })
        else:
            av_computers[int(data['computerNumber'])]=True
            print(len(requestQUEUE),"requestQUEUE")
        
        return jsonify({'message': 'Data recieved22!'})



if __name__ == '__main__':
    
    def calculate_avg_delay_time():
        global avgDelayTime
        global submissions, avgQueueLength
        if submissions != 0:
            print("Average delay time: ", avgDelayTime//submissions)
            print("Average Queue Length: ", avgQueueLength/submissions)
            submissions = 0
            avgDelayTime = 0

    t = Timer(200, calculate_avg_delay_time)
    t.start()
    app.run(debug=True, host='', port=5000)


