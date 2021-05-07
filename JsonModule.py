import json
# a = {"name": "harry", "salary": 9000, "language": "Python"}
# # conversion to JSON done by dumps() function
# b = json.dumps(a)
# print(b)  # printing the output


data = '{"var1":"harry", "var2":56}'
print(data)

parsed = json.loads(data)
print(type(parsed))

# Task 1 - json.load?


data2 = {
    "channel_name": "CodeWithHarry",
    "cars": ['bmw', 'audi a8', 'ferrari'],
    "fridge": ('roti', 540),
    "isbad": False
}

jscomp = json.dumps(data2)
print(jscomp)

# Task 2 = what is sort_keys parameter in dumps
