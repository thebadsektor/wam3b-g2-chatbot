#! /usr/bin/python3
from flask import Flask, render_template, request
import random
import csv
import os
from datetime import datetime
from botRespond import getResponse

app = Flask(__name__)

chatbotName = 'AchimBot'

#Create Log file
try:
    file = open('data/log.csv', 'r')
except IOError:
    file = open('data/log.csv', 'w')

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/get")
def get_bot_response():
    userText = request.args.get('msg')
    botReply = str(getResponse(userText))
    if botReply == "IDKresponse":
        botReply = str(getResponse('IDKnull')) ##Send the i don't know code back to the DB
    elif botReply == "getTIME":
        # botReply = "getTime()"
        botReply = datetime.now().strftime("It's already %H:%M:%S")
    elif botReply == "getDATE":
        botReply = datetime.now().strftime("The Date is %Y-%m-%d ")
        #botReply = "getDate()"
    ##Log to CSV file
    print("Logging to CSV file now")
    with open('data/log.csv', 'a', newline='') as logFile:
        newFileWriter = csv.writer(logFile)
        newFileWriter.writerow([userText, botReply])
        logFile.close()
    return botReply


if __name__ == "__main__":
    app.run()
