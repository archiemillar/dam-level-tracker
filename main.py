from flask import Flask, jsonify, render_template, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

#Connect to Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://dam_oze7_user:OaKrhuokUul1zuCDxuXUcQv5s57UK4P7@dpg-cnsmiimd3nmc73apihlg-a/dam_oze7'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


##Dam TABLE Configuration
class Dam(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    dam_name = db.Column(db.String(250), unique=True, nullable=False)
    dam_level = db.Column(db.String(250), nullable=False)


with app.app_context():
    db.create_all()
    new_dam = Dam(id=1, dam_name="Angat", dam_level="500")
    db.session.add(new_dam)
    db.session.commit()

# with app.app_context():
#     dam = Dam.query.get(1)
#     print(dam.dam_level)


@app.route("/")
def home():
    dam = Dam.query.get(1)
    return dam.dam_level


@app.route("/update-level/<dam_id>", methods=["PATCH"])
def update_level(dam_id):
    dam = Dam.query.get(dam_id)
    dam.dam_level = request.args.get("water_level")
    db.session.commit()
    return "Success"


if __name__ == '__main__':
    app.run()
