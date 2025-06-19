#method-1

i='{"name":"Alice","age":30}'
# the above line is json obj string convert => Dict

data = eval(i)
print(data)
# print(type(data))

#... method-2
import json

i = '{"name":"Alice","age":30}'

data = json.loads(i) # Convert JSON string to dictionary
doom = json.dumps(data)  # convert dict to string
print(data)
print(doom)
print(type(data))
