import json

from flask import Flask, request



app = Flask(__name__)

@app.route('/', method = ['POST'])
def credentials():
    global result
    # Function reads and store JSON dict into variable
    info = request.get_json()

    # Basic authentication
    if info['username'] == 'Jaspreet' and info['password'] == 'Password':
        print("1")
        result = 1
    elif info['username'] == 'Jordan' and info['password'] == 'Password':
        print("1")
        result = 1
    elif info['username'] == 'Arthur' and info['password'] == 'Password':
        print("1")
        result = 1
    else:
        print("0")
        result = 0
    result = 1
    return json.dumps({"result":result})

if __name__ == "__main__":
    app.run(port=5000)