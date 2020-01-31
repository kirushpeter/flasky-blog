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
    return "<h1> this is a page for {}</h1>".format(name)


if __name__ == '__main__':
    app.run(debug=True)