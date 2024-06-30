import requests

# Define the data to be sent in the POST request
data = {
    "time": 0.5,
    "src": "192.168.1.1",
    "dst": "192.168.1.2",
    "length": 100
}

# Send the POST request to the Flask server
try:
    response = requests.post('http://127.0.0.1:5000/detect', json=data)
    response.raise_for_status()  # Raise an exception for HTTP errors
    try:
        print(response.json())  # Print the JSON response from the server
    except requests.exceptions.JSONDecodeError:
        print("Response content is not valid JSON")
        print(f"Response content: {response.text}")
except requests.exceptions.RequestException as e:
    print(f"Request failed: {e}")
