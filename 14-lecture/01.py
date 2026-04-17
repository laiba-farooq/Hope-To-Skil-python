import requests

 

# Define the URL of the API endpoint

url = "https://jsonplaceholder.typicode.com/posts"

 

# Send the GET request

response = requests.get(url)

 

# Print the status code and content

print(f"Status Code: {response.status_code}")

print("Response Content:", response.json())