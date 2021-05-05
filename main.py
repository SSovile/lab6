from flask import Flask, request, jsonify, abort
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
import os

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+mysqlconnector://vlada:VLVL@localhost/iot-test-db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
ma = Marshmallow(app)


class Door(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    ser_num = db.Column(db.Integer)
    material = db.Column(db.String(40))

    def __init__(self, ser_num, material):
        self.ser_num = ser_num
        self.material = material


class DoorSchema(ma.Schema):
    class Meta:
        fields = ('id', 'ser_num', 'material')


door_schema = DoorSchema()
doors_schema = DoorSchema(many=True)


@app.route("/door", methods=["POST"])
def add_door():
    ser_num = request.json['ser_num']
    material = request.json['material']

    new_door = Door(ser_num, material)

    db.session.add(new_door)
    db.session.commit()

    return door_schema.jsonify(new_door)

@app.route("/door", methods=["GET"])
def get_door():
    all_doors = Door.query.all()
    result = doors_schema.dump(all_doors)
    return jsonify(result)

@app.route("/door/<id>", methods=["GET"])
def show_door(id):
    door = Door.query.get(id)
    if not door:
        return abort(404)
    return door_schema.jsonify(door)

@app.route("/door/<id>", methods=["PUT"])
def door_update(id):
    door = Door.query.get(id)
    if not door:
        return abort(404)
    ser_num = request.json['ser_num']
    material = request.json['material']

    door.material = material
    door.ser_num = ser_num

    db.session.commit()
    return door_schema.jsonify(door)

@app.route("/door/<id>", methods=["DELETE"])
def door_delete(id):
    door = Door.query.get(id)
    if not door:
        return abort(404)
    db.session.delete(door)
    db.session.commit()

    return door_schema.jsonify(door)

if __name__ == '__main__':
    app.run(debug=True)