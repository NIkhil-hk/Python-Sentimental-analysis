import requests

url = "https://python-sentimental-analysis.onrender.com/analyze"
data = {"text": "This is an bad project!"}
response = requests.post(url, json=data)
print(response.json())
