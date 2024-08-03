from flask import Flask, request, jsonify
from db_handler import create_connection, create_user, create_plant, create_care_task, create_growth_note

app = Flask(__name__)
database = r"db/plants.db"

@app.route('/user', methods=['POST'])
def add_user():
    conn = create_connection(database)
    user = (request.json['username'], request.json['email'], request.json['password'])
    user_id = create_user(conn, user)
    return jsonify({"user_id": user_id}), 201

@app.route('/plant', methods=['POST'])
def add_plant():
    conn = create_connection(database)
    plant = (request.json['name'], request.json['watering_schedule'], request.json['light_requirements'], request.json['user_id'])
    plant_id = create_plant(conn, plant)
    return jsonify({"plant_id": plant_id}), 201

@app.route('/care_task', methods=['POST'])
def add_care_task():
    conn = create_connection(database)
    task = (request.json['plant_id'], request.json['task_name'], request.json['task_date'])
    task_id = create_care_task(conn, task)
    return jsonify({"task_id": task_id}), 201

@app.route('/growth_note', methods=['POST'])
def add_growth_note():
    conn = create_connection(database)
    note = (request.json['plant_id'], request.json['note_date'], request.json['description'])
    note_id = create_growth_note(conn, note)
    return jsonify({"note_id": note_id}), 201

if __name__ == '__main__':
    app.run(debug=True)
