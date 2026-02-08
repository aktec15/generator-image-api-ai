import requests
import base64
import config


url = 'https://api.reve.com/v1/image/create'

headers = {
    'Authorization' : f'Bearer {config.api_key}',
    'Accept' : 'application/json',
    'Content-Type' : 'application/json'
}

data = {
    "prompt": "cat",
    "aspect_ratio": "16:9",
    "version": "latest"
}

result = requests.post(url=url, headers=headers, json=data)
print(result)
image = result.json()['image']




with open("output.png", "wb") as fh:
    fh.write(base64.decode(image))

