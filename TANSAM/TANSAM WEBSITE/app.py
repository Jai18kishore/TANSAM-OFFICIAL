from flask import Flask,render_template,request,redirect,url_for,session

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")


#HOME PAGE
@app.route("/blogsDetails")
def blogsDetails():
    return render_template("blogsdetails.html")


#OUR SOLUTIONS
@app.route("/reverseEngineering")
def reverseEngineering():
    return render_template("reverseengineering.html")


#LABS
@app.route("/productInnovation")
def productInnovation():
    return render_template("pdinnov.html")


@app.route("/innovationManufacturing")
def innovationManufacturing():
    return render_template("innovmanu.html")  


@app.route("/ar_vr")
def ar_vr():
    return render_template("arvr.html")    


@app.route("/admin")
def admin():
    return render_template("admin.html")

@app.route("/adminLogin",methods=['POST','GET'])
def adminLogin():
    if request.method == 'POST':
        username=request.form.get('username')
        password=request.form.get('password')
        print(username,password)
        if request.form.get('clicked')=='Login Now':
            return render_template("admin.html")
    return render_template("index.html")
        

if __name__ == "__main__":
    app.run(debug=True) 