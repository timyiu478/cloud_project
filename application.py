from gevent import monkey
monkey.patch_all()

from flask import Flask, render_template,request
from flask_socketio import SocketIO, emit
import app.myRDSDB as myRDSDB
from threading import Lock
import redis 
from rq import Queue
from termcolor import colored

application = Flask(__name__)
application.config.from_pyfile('app/config.py')
socketio = SocketIO(application)

thread = None
thread_lock = Lock()

r = redis.Redis()
q = Queue(connection=r)

# init database
db = myRDSDB.DB()
db.connectDB()

def writeDataBackgroundTask(data):
    print("------------- Writing Driving Data Task -------------")
    db.writeDrivingData(data)
    print("---------------- Job completed ----------------------")

def data():
    while True:
        socketio.emit('data',db.getDriversData())
        socketio.sleep(30)    

def newData(data):
    db.writeDrivingData(data)

@application.route("/")
def index():
    return render_template("index.html")

@application.route("/addData", methods=['POST'])
def addData():
    data = request.get_json()
    if data:
        print("------------- Handling New Driving Data -------------")
        print("----------- Handling Over Speeding Start ------------")
        if "isOverspeed" in data:
            socketio.emit('overspeeding',{'driverID':data["driverID"],'Time':data["Time"]})
            print(colored(data["driverID"],'red'), "is overspeeding.")
        print("----------- Handling Over Speeding End --------------")
        if "isOverspeedFinished" in data:
            socketio.emit('overspeedEnd',{'driverID':data["driverID"],'Time':data["Time"]})
            print(colored(data["driverID"],'red'), "is not overspeed.")
        from application import writeDataBackgroundTask
        job = q.enqueue(writeDataBackgroundTask,data)
        return f"Task {job.id} added to queue at {job.enqueued_at}. {len(q)} tasks in the queue"
    return "Invalid data"


@socketio.on('connect')
def test_connect():
    global thread
    with thread_lock:
        if thread is None:
            thread = socketio.start_background_task(target=data)
    socketio.emit('connect',"you are connected.")

if __name__ == "__main__":
    socketio.run(application,host="0.0.0.0",port=8080)


