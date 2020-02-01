from flask import Flask

app = Flask(__name__)

@app.route("/")

def index():
    return "<h1>Hello world!</h1>"

@app.route("/information")
def info():
    return "<h1> puppies are cute! </h1>"

#dynamic routing
@app.route("/puppy/<name>")
def puppy(name):
    return "upper case:{}".format(name.upper())


if __name__ == '__main__':
    app.run(debug=True)