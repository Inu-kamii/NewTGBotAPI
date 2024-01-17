import pip

pip.main(['install', 'psycopg2-binary'])

from flask import Flask
from flask_restful import Api
from threading import Thread

from controllers.messages_controller import MessagesController

app = Flask('')
api = Api()

api.add_resource(MessagesController, '/api/notes')
api.init_app(app)


@app.route('/')
def home():
  return "I'm alive"


def run():
  app.run(host='0.0.0.0', port=80)


def keep_alive():
  t = Thread(target=run)
  t.start()


keep_alive()
