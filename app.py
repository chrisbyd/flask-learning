 #_*_ coding:utf-8 _*_
from flask import Flask
 
app=Flask(__name__)
@app.route("/")
def index():
 	return "hello world"
@app.route("/fuck")
def fuck():
	return "fuck u"

if __name__=="__main__":
 	app.run()