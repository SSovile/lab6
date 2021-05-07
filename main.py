from flask import Flask, request, abort
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from marshmallow import fields, ValidationError

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
    id = fields.Int()
    ser_num = fields.Int(required=True)
    material = fields.String(required=True)


door_schema = DoorSchema(exclude=["id"])
doors_schema = DoorSchema(only=["id", "ser_num", "material"], many=True)


@app.route("/door", methods=["GET"])
def get_door():
    all_doors = Door.query.all()
    return doors_schema.jsonify(all_doors)


@app.route("/door/<id>", methods=["GET"])
def show_door(id):
    door = Door.query.get(id)
    if not door:
        return abort(404)
    return door_schema.jsonify(door)


@app.route("/door", methods=["POST"])
def add_door():
    try:
        received_deserialized_values = door_schema.load(request.json)
    except ValidationError:
        return abort(400)
    new_incoming_door = Door(**received_deserialized_values)
    db.session.add(new_incoming_door)
    db.session.commit()
    return door_schema.jsonify(new_incoming_door), 201


@app.route("/door/<id>", methods=["PUT"])
def door_update(id):
    door = Door.query.get(id)
    if not door:
        return abort(404)
    try:
        new_deserialized_values = door_schema.load(request.json)
    except ValidationError:
        return abort(400)
    door.__init__(**new_deserialized_values)
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
