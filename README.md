## Porject Description

This project is a complete simulation for ACPC grading system server. It is a simple archicture that can handle multiple clients at the same time. The middleware server is able to handle multiple clients at the same time with the help of 10 other servers and queues. The middleware server is responsible for handling the requests from the clients and distribute them to the other servers. The other servers are responsible for grading the submissions and sending the results back to the middleware server. The middleware server then sends the results back to the clients. The project is implemented using Python and the communication between the servers is done using HTTPS. The project is implemented using Python Flask Framework and the communication between the servers is done using HTTPS.

## How to run the project

1. Clone the project from the repository.
2. Run the following command to install the required libraries:

```
pip install -r requirements.txt
```

3. Run the following command to start the middleware server:

```
python app.py
```

4. Run the following command to start the other servers:

```
python server.py
```

5. Run the following command to start the client simulator:

```
locust
```

## Project Structure

The project is divided into the following files:

1. app.py: This file contains the middleware server implementation.
2. server.py: This file contains the other servers implementation.
3. locustfile.py: This file contains the client simulator implementation using Locust.
4. requirements.txt: This file contains the required libraries for the project.

## Project Design

The project is designed as follows:

1. The middleware server is responsible for handling the requests from the clients and distribute them to the other servers.
2. The other servers are responsible for grading the submissions and sending the results back to the middleware server.
3. The middleware server then sends the results back to the clients.
4. The communication between the servers is done using HTTPS.

## Project Implementation

The project is implemented using Python Flask Framework and the communication between the servers is done using HTTPS.

## Project Calculations

1- average delay time for each submission
2- waiting time for each submission
3- average queue length

## Project challenges

1- The project was challenging because of the complexity of the system and the need to handle multiple clients at the same time.
2- The project was challenging because of the need to handle the communication between the servers using HTTPS.
3- The project was challenging because of the need to handle the communication between the servers using queues.

## Project improvements

1- The project can be improved by adding more servers to handle more clients at the same time.
2- The project can be improved by adding more queues to handle more clients at the same time.
3- The project can be improved by adding UI dashboard to submit real code and get the results.

## Collaborators

-Amr EL-Shabacy
-Dina Ashraf
-WALID HASSAN

## License

MIT License
