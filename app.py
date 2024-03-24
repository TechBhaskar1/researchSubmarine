from flask import render_template , Flask
from paho.mqtt import client as mqtt_client

app = Flask(__name__)
broker = "broker.emqx.io"
port = 1883

topic = "topicName/iot"
username = "Bhaskar"
password = ""
client_id = "mqtt"

def connect_mqtt():
    client = mqtt_client.Client(client_id)
    client.username_pw_set(username, password)
    client.connect(broker,port)

    return client
@app.route("/")
def index():
    return render_template("index.html")

@app.route("/start" , methods = ["POST"])
def start():
    return render_template("controlPannel.html")

@app.route("/1" , methods = ["POST"])
def on():
    return render_template("1.html")

@app.route("/2" , methods = ["POST"])
def detect():
    return render_template("2.html")

@app.route("/3",methods = ["POST"])
def distance():
    return render_template("3.html")

@app.route("/4",methods = ["POST"])
def temp():
    return render_template("4.html")

@app.route("/5",methods = ["POST"])
def off():
    return render_template("5.html")

if __name__ == "__main__":
    app.run(port = 5001)