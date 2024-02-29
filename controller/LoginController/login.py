from flask import Blueprint
lg=Blueprint('login',__name__)
@lg.route('/login')
def login():
    return '1'