import json
from flask import Flask, jsonify, send_file
from Haruspex.saver.data_base import DataBase
from flask_cors import CORS
app = Flask(__name__)
import os
data_base = None


def run_api_server(host, port, database_url):
    global data_base
    data_base = DataBase(database_url)
    cors = CORS(app)
    app.run(host, port, threaded=True)


@app.route('/users', methods=['GET'])
def get_users():
    users = data_base.get_users()
    user_list = []
    for user in users:
        user_list.append({'user_id': user['user_id'], 'user_name': user['user_name']})
    return jsonify(user_list)


@app.route('/users/<user_id>', methods=['GET'])
def get_user(user_id):
    user = data_base.get_user(user_id)
    return jsonify(user)


@app.route('/users/<user_id>/snapshots', methods=['GET'])
def get_snapshots(user_id):
    snapshots_set = set()
    snapshots_of_user = data_base.get_user_snapshots(user_id)
    for snapshot in snapshots_of_user:
        snapshot_id = snapshot['timestamp']
        snapshots_set.add(snapshot_id)
    return jsonify([{"timestamp": timestamp} for timestamp in snapshots_set])


@app.route('/users/<user_id>/snapshots/<snapshot_id>', methods=['GET'])
def get_snapshot(user_id, snapshot_id):
    snapshot_list = []
    snapshot_data = data_base.get_snapshot_by_id(user_id, snapshot_id)
    snapshot_list.append({'snapshot_id': snapshot_data[0]['timestamp']})
    snapshot_list.append({'date_time': snapshot_data[0]['timestamp']})
    snapshot_list.append({'available_results': [snapshot_res['results'] for snapshot_res in snapshot_data]})
    return jsonify(snapshot_list)


@app.route('/users/<user_id>/snapshots/<snapshot_id>/<result_name>', methods=['GET'])
def get_snapshot_result(user_id, snapshot_id, result_name):
    snapshot_list = []
    snapshot_data = data_base.get_snapshot_by_result(user_id, snapshot_id, result_name)
    del snapshot_data[0]["user_id"]
    del snapshot_data[0]["_id"]
    del snapshot_data[0]["results"]
    del snapshot_data[0]["timestamp"]
    snapshot_list.append(snapshot_data[0])
    return jsonify(snapshot_list)


@app.route('/users/<user_id>/snapshots/<snapshot_id>/<result_name>/data', methods=['GET'])
def get_snapshot_result_data(user_id, snapshot_id, result_name):
    snapshot_list = []
    snapshot_data = data_base.get_snapshot_by_result(user_id, snapshot_id, result_name)
    path = snapshot_data[0]["parsed_path"]
    return send_file(path, mimetype='image/png')