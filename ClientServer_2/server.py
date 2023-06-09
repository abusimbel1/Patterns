from flask import Flask, request
app = Flask(__name__)

person_name = 'Oleksandr'

@app.route('/set_name', methods=['POST'])
def set_name():
    global person_name
    name_from_body = request.json['name']
    person_name = name_from_body
    return {'OK': 'SUCCESS'}

@app.route('/get_name', methods=['GET'])
def get_name():
    return person_name




if __name__ == '__main__':
    app.run(port=4444)