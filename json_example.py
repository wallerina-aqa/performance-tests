import json

json_data = '{"name": "Иван", "age": 30, "is_student": false}'
parsed_data = json.loads(json_data)
print(parsed_data)
print(type(parsed_data))
print(parsed_data["name"])
print(parsed_data["age"])
print(parsed_data["is_student"])

data = {"name": "Иван", "age": 30, "is_student": False}
json_string = json.dumps(data, indent=2, ensure_ascii=False)
print(json_string)
print(type(json_string))

with open("json_example.json", encoding="utf-8") as file:
    data = json.load(file)
    print(data)

with open("data.json", "w", encoding="utf-8") as file:
    json.dump(data, file, indent=2, ensure_ascii=False)
