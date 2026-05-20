from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/lumeofilters.html")
def lumeofilters():
    return render_template("lumeofilters.html")

@app.route("/quickreels.html")
def lumeofilters():
    return render_template("quickreels.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)