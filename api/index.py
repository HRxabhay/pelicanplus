from flask import Flask

app = Flask(__name__)
 
@app.route("/api/python")
def hello_world():
 return "mscmsmc"

if __name__ == "__main__":
    app.run()
