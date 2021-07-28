import json
from app import db


def create_fixture(path_file):
    with open(path_file, 'r', encoding='utf-8') as f:
        data_fixtures = json.load(f)
    for row in data_fixtures:
        db.forms.insertOne({"age": 1}, {"unique": True})
    return 'ok'


if __name__ == "__main__":
    create_fixture('fixture.json')
