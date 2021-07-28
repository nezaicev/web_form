import os
import json
from flask import request
from flask import Flask, jsonify
from flask_pymongo import PyMongo

import utils

FIXTURE_PATH='fixture.json'
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


@app.route('/load_dump')
def test_dump():
    if os.path.exists(FIXTURE_PATH):
        if not list(db.forms.find()):
            with open(FIXTURE_PATH, 'r', encoding='utf-8') as f:
                data_fixtures = json.load(f)
            for row in data_fixtures:
                db.forms.insert_one(row, {'unique': True})
            return jsonify({'message':'ok'})
        else:
            return jsonify({'message': 'DB not empty'})
    else:
        jsonify({'message':'File  not find'.format(FIXTURE_PATH)})


@app.route('/get_form', methods=['POST'])
def get_form():
    tmp_form = {}
    fields = dict(request.args)
    for key, value in fields.items():
        tmp_form[key] = utils.validate_field(value)
    results = list(db.forms.find(tmp_form, {'_id': 0, 'name': 1}))
    if results:
        return jsonify(results)
    else:
        return jsonify(tmp_form)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)