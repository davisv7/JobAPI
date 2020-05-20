from flask import Flask, request
from flask_json import FlaskJSON, as_json
import helperfunctions as hf
app = Flask(__name__)
FlaskJSON(app)


@app.route('/api/reset')
@as_json
def reset():
    try:
        hf.reset_db()
        response = {
            "reset_status_code": "1"
        }
    except Exception as e:
        print(e, flush=True)
        response = {
            "reset_status_code": "0"
        }
    return response


@app.route('/api/insert_job', methods=['GET', 'POST'])
@as_json
def insert_job():
    job = request.get_json()
    try:
        hf.insert_job(job)
        response = {
            "reset_status_code": "1"
        }
    except Exception as e:
        print(e, flush=True)
        response = {
            "reset_status_code": "0"
        }
    return response

@app.route('/api/insert_config', methods=['GET', 'POST'])
@as_json
def insert_config():
    config = request.get_json()
    try:
        hf.insert_config(config)
        response = {
            "reset_status_code": "1"
        }
    except Exception as e:
        print(e, flush=True)
        response = {
            "reset_status_code": "0"
        }
    return response

@app.route('/api/insert_jobTemplate', methods=['GET', 'POST'])
@as_json
def insert_template():
    jobTemp = request.get_json()
    try:
        hf.insert_template(jobTemp)
        response = {
            "reset_status_code": "1"
        }
    except Exception as e:
        print(e, flush=True)
        response = {
            "reset_status_code": "0"
        }
    return response

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8088, debug=True, threaded=True)  # threaded
