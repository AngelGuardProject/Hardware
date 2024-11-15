import requests

def push():
    notification_data = {"title": "아이 울음 감지", "body": "아이 상태를 확인해 주세요"}
    url = f"http://34.47.76.73:3000/push/send/{UUID}"
    headers = {"Content-Type": "application/json"}
    try:
        response = requests.post(url, json=notification_data, headers=headers)
        response.raise_for_status()  # Check for HTTP request errors
        return response.json()  # Return the response in JSON format
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
        return None

# Example usage
UUID = 0
response = push()
if response:
    print("Response from server:", response)
