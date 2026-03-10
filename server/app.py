import os
from flask import Flask, request, current_app, g, make_response

app = Flask(__name__)

@app.before_request
def app_path():
    g.path = os.path.abspath(os.getcwd())

@app.route('/')
def index():
    host_name = request.headers.get('Host')
    app_name = current_app.name
    response_body = f'''
    <h1> This page is being hosted on {host_name}</h1>
    <h2>The name of this application is <strong>{app_name}<strong></h2>
    <h3>The path to this application on the user's device is {g.path}</h3>
    <h4>Updated!</h4>
    '''
    status_code = 200
    headers = {}
    return make_response(response_body, status_code, headers)

       

if __name__ == '__main__':
    app.run(port = 5555, debug = True)

