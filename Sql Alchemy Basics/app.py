from flask import Flask, render_template,request
from flask_sqlalchemy  import SQLAlchemy 


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db =SQLAlchemy(app)

class Item(db.Model):
    id = db.Column(db.Integer ,primary_key=True)
    name = db.Column(db.String(100), nullable=False)


@app.route("/query")
def insert_values():
    
    id = request.args.get('id')
    name = request.args.get('name')
    if not id or not name:
        return {"error": "id and name are required"}, 400
    new_item = Item(id=id, name=name)
    db.session.add(new_item)
    db.session.commit()
    return {"message": "Item added successfully"}, 201


@app.before_request
def create_tables():
    db.create_all()

if __name__ =='__main__':
    app.run(debug=True)