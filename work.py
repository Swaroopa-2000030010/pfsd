
from flask import Flask,render_template,url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///zone.db'
db=SQLAlchemy(app)

class Menus(db.Model):
    item=db.Column(db.String(32),primary_key=True,unique=True,nullable=False,default='default.jpg')
    avalible = db.Column(db.String(32),  unique=False, nullable=False, default='default.jpg')
    price = db.Column(db.String(32),  unique=False, nullable=False, default='default.jpg')













menus = [
    {
        "item":"Pasta",
        "avalible":"Yes",
        "price":"550"
    },
    {
        "item": "Burger",
        "avalible": "No",
        "price": "300"
    },
    {
        "item": "Pizza",
        "avalible": "Yes",
        "price": "850"
    }
]





@app.route("/")

@app.route("/home")
def home():
    return render_template("home.html",title = "home")
@app.route("/menu")
def menu():
    return render_template("menu.html",title ="menu",menus = Menus.query.all())

@app.route("/customer")
def customer():
    return render_template("customer.html",title = "customer")
@app.route("/service")
def service():
    return render_template("service.html",title = "service")
if __name__=='__main__':
    app.run(debug=True)







