import requests

url = "http://127.0.0.1:8000/analyze"
data = {"text": "This is an bad project!"}
response = requests.post(url, json=data)
print(response.json())
