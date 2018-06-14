from flask import Flask, render_template, url_for

myapp = Flask(__name__)
@myapp.route("/")
def hello():
    return render_template("index.html")

if __name__ == "__main__":
    myapp.run(debug=True)

