from flask import Flask
from flask import request
app = Flask(__name__)

@app.route('/')
def credentials():
    username = request.args.get('username')
    password = request.args.get('password')
    print( username, password)
    result = 0
    # Basic authentication
    if username == 'Jaspreet' and password == 'Password':
        print("1")
        result = '1'
    elif username == 'Jordan' and password == 'Password':
        print("1")
        result = '1'
    elif username == 'Arthur' and password == 'Password':
        print("1")
        result = '1'
    else:
        print("0")
        result = '0'
    return result

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)