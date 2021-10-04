from flask import Flask
from flask import request
from flask import jsonify
from flask_cors import CORS
from werkzeug import useragents
import string
import random
import json
from random import randint

app = Flask(__name__)
CORS(app)

users = { 
   'users_list' :
   [
      { 
         'id' : 'xyz789',
         'name' : 'Charlie',
         'job': 'Janitor',
      },
      {
         'id' : 'abc123', 
         'name': 'Mac',
         'job': 'Bouncer',
      },
      {
         'id' : 'ppp222', 
         'name': 'Mac',
         'job': 'Professor',
      }, 
      {
         'id' : 'yat999', 
         'name': 'Dee',
         'job': 'Aspring actress',
      },
      {
         'id' : 'zap555', 
         'name': 'Dennis',
         'job': 'Bartender',
      }
   ]
}

def id_generator():
   new_id = random.choice(string.ascii_lowercase) + random.choice(string.ascii_lowercase) + random.choice(string.ascii_lowercase) + str(randint(100, 999))
   return new_id

@app.route('/users/<id>', methods=['GET', 'DELETE'])
def get_user(id):
   if id :
      if request.method == 'GET':
         for user in users['users_list']:
            if user['id'] == id:
               return user
         return ({})
      elif request.method == 'DELETE':
         userToDel = request.get_json()
         for currUser in users['users_list']:
            if currUser['id'] == id:
               users['users_list'].remove(currUser)
         resp = jsonify(success=True)
         resp.status_code = 204
         return resp
   return users

@app.route('/users', methods=['GET', 'POST', 'DELETE'])
def get_users():
   if request.method == 'GET':
      search_username = request.args.get('name')
      search_job = request.args.get('job')
      if search_username and search_job:
         subdict = {'users_list' : []}
         for user in users['users_list']:
            if (user['name'] == search_username and user['job'] == search_job):
               subdict['users_list'].append(user)
         return subdict
      elif search_username :
         subdict = {'users_list' : []}
         for user in users['users_list']:
            if user['name'] == search_username:
               subdict['users_list'].append(user)
         return subdict
      return users

   elif request.method == 'POST':
      userToAdd = request.get_json()
      new_id = id_generator()
      userToAdd['id'] = new_id

      users['users_list'].append(userToAdd)
      resp = jsonify(userToAdd)
      resp.status_code = 201 #optionally, you can always set a response code. 
      # 200 is the default code for a normal response
      return resp

def get_name_and_job():
   search_username = request.args.get('name') #accessing the value of parameter 'name'
   if search_username :
      subdict = {'users_list' : []}
      for user in users['users_list']:
         if user['name'] == search_username:
            subdict['users_list'].append(user)
      return subdict
   return users

