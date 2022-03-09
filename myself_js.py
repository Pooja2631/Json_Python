import json
python_obj = {
  "name": "Pooja",
  "name1": "deepti",
  "class":"I",
  "age": 18 
}
print(type(python_obj))
j_data = json.dumps(python_obj)
print(j_data)