from flask import  Flask
from config.config import conf
from controller import login,register
RouterList=[login.lg,register.reter]
def create_app()-> object:
    app=Flask(__name__)
    app=AppBluePrint(app=app,RouterList=RouterList)
    return app
def AppBluePrint(app: object,RouterList)-> object:
    for i in RouterList:
        app.register_blueprint(i)
    return app