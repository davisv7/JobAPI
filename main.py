from flask import Flask
from flask_json import FlaskJSON, as_json
from helperfunctions import reset_db, loginToDB

app = Flask(__name__)
FlaskJSON(app)


@app.route('/api/reset')
@as_json
def reset():
    try:
        reset_db()
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
