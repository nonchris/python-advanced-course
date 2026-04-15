import requests

resp: requests.Response = requests.get('https://avatars.githubusercontent.com/u/58270603?v=4')

if resp.status_code != 200:
    print(f"There was an error: {resp.status_code} - exiting")
    exit(1)

message = resp.content
print(message)
with open("img.png", "wb") as f:
    f.write(resp.content)

