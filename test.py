import json
current_time= "1234"
first = current_time[0]+".json"
with open(first, 'r') as file:
                first = json.load(file)
print(first)