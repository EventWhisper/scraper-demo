from flask import Flask, jsonify, request
from prometheus_flask_exporter import PrometheusMetrics
from flask_httpauth import HTTPTokenAuth
import random
from scraper import Run
import os

APP_TOKEN = os.environ.get('APP_TOKEN', "TOKEN_NOT_SET")
APP_VERSION = os.environ.get('APP_VERSION', "0.0.0")

app = Flask(__name__)
metrics = PrometheusMetrics(app)
metrics.info('app_info', 'Application info', version=APP_VERSION)
info_events_last_run = metrics.info('events_found_last_run', 'Events found in the last run')
auth = HTTPTokenAuth(scheme='Bearer')

@app.route('/')
@auth.login_required
def index():
    return "Hello, World!"


@app.route('/scrape')
@auth.login_required
def scrape():
    events = Run()
    info_events_last_run.set(len(events))
    json_obj_arr = []
    for event in events:
        json_obj_arr.append(event.toJSON())
    
    return "[" + ",".join(json_obj_arr) + "]"

@app.route('/metrics')
@auth.login_required
def metrics():
    return metrics

@auth.verify_token
def verify_token(token):
    print(token)

    if token == APP_TOKEN:
        return True
    return False

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)