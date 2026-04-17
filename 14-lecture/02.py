import requests

 

# API URL for POST request

url = "https://jsonplaceholder.typicode.com/posts"

 

# Data to send with the request

data = {

    "title": "New Post",

    "body": "This is a new post created using the requests module.",

    "userId": 1

}

 

# Send the POST request

response = requests.post(url, json=data)

 

# Print status code and the response content

print(f"Status Code: {response.status_code}")

print("Response Content:", response.json())