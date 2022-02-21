import json

def credentials():
    # Function reads and store JSON dict into variable
    with open('credential.json', 'r') as file:
        info = file.read()
        info = json.loads(info)

    # Basic authentication
    if info['username'] == 'Jaspreet' and info['password'] == 'Password':
        print("1")
        return 1
    elif info['username'] == 'Jordan' and info['password'] == 'Password':
        print("1")
        return 1
    elif info['username'] == 'Arthur' and info['password'] == 'Password':
        print("1")
        return 1
    else:
        print("0")
        return 0


if __name__ == "__main__":
    auth = credentials()