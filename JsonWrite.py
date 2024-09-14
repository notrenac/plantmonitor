import json

# with open('test.json', 'r') as openfile:
 
#     # Reading from json file
#     json_object = json.load(openfile)

# print(json_object)
# print(type(json_object))

humidity = 41
temperature = 27
moisture = 15

dictionary = {
    'Plant1': {'humidity': humidity, 'temperature': temperature, 'moisture': moisture}
}

with open("test.json", "w") as outfile:
    json.dump(dictionary, outfile)