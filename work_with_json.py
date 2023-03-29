import json


def writing_in_json(data, filename):
    data = json.dumps(data)
    data = json.loads(str(data))
    with open(filename, 'w', encoding='utf-8') as file:
        json.dump(data, file, indent=4)


def reading_json(filenme):
    with open(filenme, 'r', encoding='utf-8') as file:
        return json.load(file)
