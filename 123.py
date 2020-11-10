import requests

url = "https://hearthstoneapi.com/webhook/slack/cards"

payload  = {}
headers= {}

response = requests.request("GET", url, headers=headers, data = payload)

data=json.loads(response.text)
print(data)
