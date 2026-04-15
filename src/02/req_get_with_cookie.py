import requests

url = "http://127.0.0.1:3001"
data = {"username": "CyberChris"}

r = requests.post(f"{url}/register", params=data)

if r.status_code != 200:
    print(f"There was an error: {r.status_code} - exiting")
    exit(1)

print("Registration successful!")
user_cookie = r.cookies.get("user_id")

print(f"user_id cookie: {user_cookie}")

who_am_i = requests.get(f"{url}/whoami", cookies={"user_id": user_cookie})

print(who_am_i.text)




