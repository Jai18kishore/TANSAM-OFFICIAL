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

@app.route("/naanmudhalvan")
def naanmudhalvan():
    return render_template("nanmudhalvan.html")

@app.route("/adminLogin")
def adminLogin():
    return render_template("login.html")

@app.route("/adminIndex",methods=['POST'])
def adminIndex():
    if request.method == 'POST':
        username=request.form.get('username')
        password=request.form.get('password')
        print(username,password)
        if username=='admin' and password=='admin':
            return render_template("admin.html")
    return render_template("index.html")
        
@app.route("/adminBlogs")




if __name__ == "__main__":
    try:
        app.run(debug=True)
    except:
        print("Error in running the app")