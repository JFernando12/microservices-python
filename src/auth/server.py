import jwt, datetime, os
from flask import Flask, request
from flask_mysqldb import MySQL

server = Flask(__name__)
mysql = MySQL(server)

# config
server.config['MYSQL_HOST'] = os.getenv('MYSQL_HOST')
server.config['MYSQL_USER'] = os.getenv('MYSQL_USER')
server.config['MYSQL_PASSWORD'] = os.getenv('MYSQL_PASSWORD')
server.config['MYSQL_DB'] = os.getenv('MYSQL_DB')
server.config['MYSQL_PORT'] = os.getenv('MYSQL_PORT')

# routes
@server.route('/login', methods=['POST'])
def login():
    auth = request.authorization
    if not auth:
        return 'Missing credentials', 401
    
    # check db for username and password
    