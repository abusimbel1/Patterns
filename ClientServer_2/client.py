import urllib.request
import json

def get_name():
    url = 'http://localhost:4444/get_name'
    response = urllib.request.urlopen(url)
    return response.read().decode()

def post_message(new_name):
    url = 'http://localhost:4444/set_name'
    data = {'name': new_name}
    data = json.dumps(data).encode()
    req = urllib.request.Request(url, data=data, headers={
                                 'Content-Type': 'application/json'})
    response = urllib.request.urlopen(req)
    return response


if __name__ == '__main__':
    while True:
        new_name = input('Enter new name...').strip()
        if new_name:
            post_message(new_name)
        print('New Name:', get_name())