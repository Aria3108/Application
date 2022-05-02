from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")
    
@app.route("/dashboard", methods=["POST"])
def dashboard():
    name = request.form.get("nombre")
    direccion = request.form.get("direccion")
    ocupacion = request.form.get("ocupacion")
    nacionalidad = request.form.get("nacionalidad")
    email = request.form.get("email")
    contra = request.form.get("contra")
    date=request.form.get("date")
    return render_template("dashboard.html",name=name, direccion = direccion,
    ocupacion=ocupacion, nacionalidad = nacionalidad, email=email,
    contra=contra,date=date)


   
