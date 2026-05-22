from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/lumeofilters.html")
def lumeofilters():
    return render_template("lumeofilters.html")

@app.route("/quickreels.html")
def quickreels():
    return render_template("quickreels.html")

@app.route("/scantextpdf.html")
def scantextpdf():
    return render_template("scantextpdf.html")

@app.route("/voicent.html")
def voicent():
    return render_template("voicent.html")

@app.route("/docsnap.html")
def voicent():
    return render_template("docsnap.html")



if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)