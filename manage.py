import json
from app import db


def create_fixture(path_file):
    if not list(db.forms.find()):
        with open(path_file, 'r', encoding='utf-8') as f:
            data_fixtures = json.load(f)
        for row in data_fixtures:
            db.forms.insert_one(row, {"unique": True})
        return 'ok'


if __name__ == "__main__":
    create_fixture('fixture.json')
