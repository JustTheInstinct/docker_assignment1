from flask import Flask

from auth.auth import credentials

app = Flask(__name__)

@app.route('/')
def test():
    auth_check = credentials
    if auth_check:
        print("Valid")
        return "Validated"
    else:
        print("Invalid")
        return "Invalid credentials"

if __name__ == "__main__":
    test()