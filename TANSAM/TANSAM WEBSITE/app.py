from flask import Flask,render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/productInnovation")
def productInnovation():
    return render_template("pdinnov.html")

@app.route("/innovationManufacturing")
def innovationManufacturing():
    return render_template("innovmanu.html")  

@app.route("/ar_vr")
def ar_vr():
    return render_template("arvr.html")    

if __name__ == "__main__":
    app.run(debug=True) 