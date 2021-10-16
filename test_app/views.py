from test_app import app

@app.route("/")
def show():
    return "Hello World."