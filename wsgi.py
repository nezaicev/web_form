from  app import app
from manage import create_fixture

if __name__ == "__main__":
    create_fixture('fixture.json')
    app.run(host="0.0.0.0", port=8080, debug=True)