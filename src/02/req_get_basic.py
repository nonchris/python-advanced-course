import requests

resp: requests.Response = requests.get('https://httpbin.org/ip')

if resp.status_code != 200:
    print(f"There was an error: {resp.status_code} - exiting")
    exit(1)

message = resp.json()
print(message)
