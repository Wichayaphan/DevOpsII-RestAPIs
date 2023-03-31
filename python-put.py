import requests
api_url = "https://jsonplaceholder.typicode.com/todos/1"

response = requests.get(api_url)
print(response.json())

todo = {
    "userID" : 1,
    "id" : 1,
    "title" : "Wichayaphan Traithipthomrongchoke",
    "completed" : True
    }

response = requests.put(api_url, json=todo)

print(response.json())
print(response.status_code)