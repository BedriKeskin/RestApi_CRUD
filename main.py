from flask import Flask, request, jsonify

app = Flask(__name__)

Practice = [
    {
        "id": "3136e3cd-c90c-48bb-b9a9-60ca68382ad7",
        "title": "Say hello with python",
        "problem": "Print hello world in Python using print",
        "point": 1,
        "level": "beginner",
        "language": "python",
        "input": "",
        "expected_output": "Hello World"
    },
    {
        "id": "1ff26d62-e748-4907-bccf-cf2eec4ec06b",
        "title": "Arithmetic Operators - Sum",
        "problem": "Sum two numbers",
        "point": 2,
        "level": "beginner",
        "language": "python",
        "input": "5,6",
        "expected_output": "11"
    },
    {
        "id": "d07cb6ee-af91-4d0f-abd7-efe1693a8d3f",
        "title": "Loops",
        "problem": "Print the square of each number in the loop step",
        "point": 2,
        "level": "beginner",
        "language": "python",
        "input": "4",
        "expected_output": "0,1,4,9"
    }
]


@app.route('/', methods=['GET'])
def home():
    return "Simple Rest API CRUD (create, read, update, delete) example"


@app.route('/all', methods=['GET'])
def read_all():
    return jsonify(Practice)


@app.route('/read', methods=['GET'])
def read():
    uuid = request.args['id']
    results = []
    for item in Practice:
        if item['id'] == uuid:
            results.append(item)
    return jsonify(results)


@app.route('/create', methods=['POST'])
def create():
    uuid = request.json['id']
    title = request.json['title']
    problem = request.json['problem']
    point = int(request.json['point'])
    level = request.json['level']
    language = request.json['language']
    input = request.json['input']
    expected_output = request.json['expected_output']

    newItem = {'id': uuid, 'title': title, 'problem': problem, 'point': point, 'level': level, 'language': language,
               'input': input, 'expected_output': expected_output}

    Practice.append(newItem)
    return "New item added"


@app.route('/update', methods=['POST'])
def update():
    uuid = request.args['id']
    for item in Practice:
        if item['id'] == uuid:
            Practice.remove(item)  # at first remove item and create with the same id

            title = request.json['title']
            problem = request.json['problem']
            point = int(request.json['point'])
            level = request.json['level']
            language = request.json['language']
            input = request.json['input']
            expected_output = request.json['expected_output']

            newItem = {'id': uuid, 'title': title, 'problem': problem, 'point': point, 'level': level,
                       'language': language,
                       'input': input, 'expected_output': expected_output}

            Practice.append(newItem)
    return "Updated"


@app.route('/delete', methods=['POST'])
def delete():
    uuid = request.args['id']
    for item in Practice:
        if item['id'] == uuid:
            Practice.remove(item)
    return "Deleted"


if __name__ == '__main__':
    app.run()
