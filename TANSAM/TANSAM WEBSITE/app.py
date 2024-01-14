from flask import Flask,render_template,request,redirect,url_for,session
import os
app = Flask(__name__)

@app.route("/")
def index():
    return render_template("admin.html")


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
            return redirect(url_for('admin'))
    return render_template("index.html")


@app.route("/admin")
def admin():
    return render_template("admin.html")


@app.route("/adminPosts/<Type>")
def adminPosts(Type):
    return render_template("adminblogs.html",type=Type)        


@app.route('/postDetails/<Type>', methods=['POST'])
def postDetails(Type):
    print(Type)
    if request.method=='POST':
        print(Type)
        title=request.form.get('blogstitle')
        date=request.form.get('blogsdate')
        author=request.form.get('blogsauthor')
        image=request.files['blogsimage']
        #save image in static
        image.save('static')
        content=request.form.get('blogscontent')
        print(title,date,author,content)
        #create a notepad with name of the titile and write all the content in it
        #save the notepad in static
        fp=open('/static/'+title+'.txt','w')
        fp.write(date+"\n\n")
        fp.write(author+"\n\n")
        fp.write(content)
        fp.close()
        
        
    return render_template("adminblogs.html")

if __name__ == "__main__":
    try:
        app.run(debug=True)
    except:
        print("Error in running the app")