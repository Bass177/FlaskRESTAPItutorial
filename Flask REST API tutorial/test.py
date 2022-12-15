import requests 

BASE = "http://127.0.0.1:5000/"

data = [
{"likes": 657, "views":4670, "name":"How to make Scotch Rock Drinks"},
{"likes": 1534, "views":20000, "name":"The Finer Points of Weaving Gasoline"},
{"likes": 3405, "views":10000, "name":"Hunting Crag-Runners in the Everglades"},
]

for i in range(len(data)):
    response = requests.put(BASE + "video/" + str(i), data[i])
    print(response) 


input()
response = requests.get(BASE + "video/6")
print(response.json())