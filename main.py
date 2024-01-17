import os

from dotenv import load_dotenv
from flask import Flask
from flask_restful import Api
import pip

pip.main(['install', 'flask'])
pip.main(['install', 'Flask-RESTful'])
pip.main(['install', 'psycopg2-binary'])
pip.main(['install', 'python-dotenv'])


from controllers.messages_controller import MessagesController

app = Flask('')
api = Api()

load_dotenv()

api.add_resource(MessagesController, '/api/notes')
api.init_app(app)

@app.route('/')
def home():
  return "I'm alive"

if __name__ == '__main__':
    app.run(debug=True, port=3000, host='localhost')
