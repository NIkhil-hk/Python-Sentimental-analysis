import requests

url = "https://python-sentimental-analysis.onrender.com/analyze"  # Replace with your actual Render URL
data = {"text": "I is awesome!"}

response = requests.post(url, json=data)

print("Status Code:", response.status_code)  # Print HTTP status
print("Response Text:", response.text)  # Print raw response
