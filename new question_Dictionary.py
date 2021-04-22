# Python Dictionary
import json
client = {
    "name": "Nora",
    "age": 56,
    "id": "45355",
    "eye_color": "green",
    "wears_glasses": False
}
# Get a JSON formatted string
print(json.dumps(client))
