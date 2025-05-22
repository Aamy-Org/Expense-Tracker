from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)        

class Item(db.Model):   
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)        

class ItemDetails(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)

@app.route("/",methods=["GET","POST"])
def form_example():
    if request.method == "POST":
        name= request.form.get("name")
        id= request.form.get("id")
        if not name or not id:
            return {"error": "id and name are required"}, 400
        new_item = ItemDetails(id=id, name=name)
        db.session.add(new_item)
        try:
            db.session.commit()
            return {"message":"success"}, 201
        except Exception as e:
            db.session.rollback()
            return {"error": str(e)}, 500
    return render_template("form2.html")

@app.before_request
def create_tables():
    db.create_all()

if __name__=="__main__":
    app.run(debug=True) 

