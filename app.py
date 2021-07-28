import os
from flask import request
from flask import Flask, jsonify
from flask_pymongo import PyMongo

import utils

app = Flask(__name__)
app.config["MONGO_URI"] = 'mongodb://{}:{}/{}'.format(
    os.environ['MONGO_DB_ADDR'],
    os.environ['MONGO_DB_PORT'],
    os.environ['MONGODB_DATABASE'],
)
mongodb_client = PyMongo(app)
db = mongodb_client.db


@app.route('/test')
def test():
    return jsonify(message="success")


@app.route('/get_form', methods=['POST'])
def get_form():
    tmp_form = {}
    fields = dict(request.args)
    for key, value in fields.items():
        tmp_form[key] = utils.validate_field(value)
    results = list(db.forms.find(tmp_form, {'_id': 0, 'name': 1}))
    # results = db.forms.findOne(tmp_form, {'_id': 0, 'name': 1})
    print(results)
    print(list(results))
    if results:
        return jsonify(results)
    else:
        return jsonify(tmp_form)


# @app.route("/add_one", methods=['POST'])
# def add_one():
#     db.forms.insert_one(dict(request.args))
#     return jsonify(message="success")
