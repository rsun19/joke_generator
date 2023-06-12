from joke_generator.models import Jokes, CleanJokes
from flask import render_template, url_for, abort, redirect, request, make_response, jsonify
from joke_generator import app, db
from functools import wraps
from sqlalchemy import and_, func, or_, desc
from datetime import datetime
from decouple import config

@app.route("/")
@app.route("/home")
def home():
    return "Welcome to the API! A webpage will be coming soon :)"

@app.route("/api")
def api():
    return "Hello, I am very healthy!"

@app.route("/api/joke", methods=['GET'], endpoint='joke')
def joke():
    if request.method == 'GET':
        query = request.headers.get('query')
        output = []
        results = Jokes.query.filter(Jokes.joke.ilike(f"%{query}%")).order_by(func.random()).first()
        if results:
            result_details = Jokes.serialize(results)
            output.append(result_details)
        else:
            backup_query = Jokes.query.order_by(func.random()).first()
            result_details = Jokes.serialize(backup_query)
            output.append(result_details)       
        return jsonify(output), 200
    else:
        return jsonify({'message': 'Invalid method'}), 401

@app.route("/api/cleanjoke", methods=['GET'], endpoint='cleanjoke')
def cleanjoke():
    if request.method == 'GET':
        query = request.headers.get('query')
        output = []
        results = CleanJokes.query.filter(CleanJokes.joke.ilike(f"%{query}%")).order_by(func.random()).first()
        if results:
            result_details = CleanJokes.serialize(results)
            output.append(result_details)
        else:
            backup_query = CleanJokes.query.order_by(func.random()).first()
            result_details = CleanJokes.serialize(backup_query)
            output.append(result_details)       
        return jsonify(output), 200
    else:
        return jsonify({'message': 'Invalid method'}), 401
