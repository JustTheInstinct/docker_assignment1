import json, requests

result = 0

def credentials():
    global result
    # Function reads and store JSON dict into variable
    info = requests.get('http://localhost:5000')

    # with open('credential.json', 'r') as file:
        # info = file.read()
        # info = json.loads(info)

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

    #requests.post('http://:')


if __name__ == "__main__":
    credentials()