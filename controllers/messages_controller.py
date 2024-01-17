from flask import request
from flask_restful import Resource

from persistance.db_context import DBContext


class MessagesController (Resource):
    def get(self):
        day = request.args.get('day', None)
        month = request.args.get('month', None)
        year = request.args.get('year', None)
        print(day, month, year)
        if day is not None and month is not None and year is not None:
            query = "SELECT * FROM Messages WHERE day=%s AND month=%s AND year=%s"
            params = (day, month, year)
        else:
            query = 'SELECT * FROM Messages'
            params = None

        context = DBContext()
        notes = context.fetch_all(query, params)
        return {'notes': notes}

    def post(self):
        data = request.get_json()
        day = data['day']
        month = data['month']
        year = data['year']
        message = data['text']

        query = "INSERT INTO Messages (day, month, year, text) VALUES (%s, %s, %s, %s)"
        params = (day, month, year, message)

        context = DBContext()
        context.execute_query(query, params)
        return {'message': 'Note added successfully'}

    def put(self):
        data = request.get_json()
        day = data['day']
        month = data['month']
        year = data['year']
        new_message = data['text']

        query = "UPDATE Messages SET text=%s WHERE day=%s AND month=%s AND year=%s"
        params = (new_message, day, month, year)

        context = DBContext()
        context.execute_query(query, params)
        return {'message': 'Note updated successfully'}

    def delete(self):
        data = request.get_json()
        day = data['day']
        month = data['month']
        year = data['year']
        query = "DELETE FROM Messages WHERE day=%s AND month=%s AND year=%s"
        params = (day, month, year)

        context = DBContext()
        context.execute_query(query, params)
        return {'message': 'Note deleted successfully'}