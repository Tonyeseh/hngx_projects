#!/usr/bin/python3
"""Simple flask app with one route"""
from flask import Flask, jsonify, request

from datetime import datetime, timezone

app = Flask(__name__)

@app.route('/api')
def api_route():
    """defines the /api route"""
    name = request.args.get('slack_name')
    track = request.args.get('track')
    date_format = "%Y-%m-%dT%H:%M:%SZ"
    d = datetime.now(timezone.utc)
    response =  jsonify({
        "slack_name": "esehtony",
        "current_day": get_weekday(d),
        "utc_time": d.strftime(date_format),
        "track": "backend",
        "github_file_url": "https://github.com/Tonyeseh/hngx_projects/blob/main/taskOne/app.py",
        "github_repo_url": "https://github.com/Tonyeseh/hngx_projects",
        "status_code": 200
    })
    response.headers['Content_Type'] = "application/json"
    return response, 200

def get_weekday(date):
    """returns the weekday in string"""
    weekday = date.weekday()
    if weekday == 0:
        return "Monday"
    elif weekday == 1:
        return "Tuesday"
    elif weekday == 2:
        return "Wednesday"
    elif weekday == 3:
        return "Thursday"
    elif weekday == 4:
        return "Friday"
    elif weekday == 5:
        return "Saturday"
    return "Sunday"

if __name__ == "__main__":
    app.run()
