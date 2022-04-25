from flask import (
    Flask,
    request
)

from datetime import datetime

from app.database import user


app = Flask(__name__) #app is an object created from flask
VERSION = "1.0.0" #global variable VERSION

@app.get("/version") #decorators a function that wraps another function
def get_version():
    out = {
        "server_time": datetime.now().strftime("%F %h:%M:%S"),
        "version": VERSION
    }
    return out

@app.get("/users/")
def get_all_users():
    user_list = user.scan()
    resp ={#python dictionary  
        "status": "ok",
        "message":"success",
        "user": user_list
    }
    return resp

@app.get("/users/<int:pk>/")#this end point with "int"will tell flask to recieve a parameter in our view funiction
def get_user_by_id(pk):
    target_user = user.select_by_id(pk)
    resp ={#python dictionary  
        "status": "ok",
        "message":"success"
    }
    if target_user:#if taarget user is not empty
        resp["user"]= target_user
        return resp #a 200 code by default will return
    else:
        resp ["status"]= "error"
        resp["message"]= "User not found"
        return resp, 404

@app.post("/users/")
def create_user():
    user_data = request.json            #request is a Flask contxt object
    user.insert(user_data)
    return "",204            #no conent status the operation was succesfull          
                            #but there is no conent to display or return
@app.put("/users/<int:pk>/")
def update_user(pk):
    user_data = request.json    #request is a Flask context objects
    user.insert(pk, user_data)
    return "",204

@app.delete("/users/<int:pk>/")
def deactivate_user(pk):
    user.deactivate(pk)
    return "", 204