from flask import Flask, request, jsonify
import requests
from multiprocessing import Process
import os
import threading
import time
import random
def create_app(port):
    app = Flask(__name__)
    arr=[]

    @app.route('/')

    def home():
        return f"Server running on port {port}"
    
        
        if request.json:
            # sleep for 10 seconds
            print("recieved",port)
            # thread function to sleep for 10 seconds
            def get_time():
                print("sleeping for 10 seconds")
                start_time = time.time()
                while time.time() - start_time < 10:
                    pass

                print("time is up")
                requests.post(f"http://localhost:5000/api/device-5000/recieved",json={"computerNumber":f'{port-5001}'})
            threading.Thread(target=get_time).start()

            
            return  jsonify({"message":"Data recieved!"})
    @app.route(f"/api/device-{port}/recieved",methods=["POST"])

    def home1():
        
        if request.json:
            # sleep for 10 seconds
            print("recieved",port)
            # thread function to sleep for 10 seconds
            r = random.randint(37, 47)
            def get_time():
                print(f"sleeping for {r} seconds")
                start_time = time.time()
                while time.time() - start_time < r:
                    pass

                print("time is up")
                requests.post(f"http://localhost:5000/api/device-5000/recieved",json={"computerNumber":f'{port-5001}'})
            threading.Thread(target=get_time).start()

            
            return  jsonify({"message":"Data recieved!"})
            
        
    app.run(port=port,threaded=True)

if __name__ == '__main__':
    processes = []
    for port in range(5001, 5011):  # Start servers on ports 5000-5009
        p = Process(target=create_app, args=(port,))
        processes.append(p)
        p.start()

    for p in processes:
        p.join()
    