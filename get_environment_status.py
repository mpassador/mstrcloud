import requests
  
url = "https://developer.customer.cloud.microstrategy.com/api/environments/states"

payload = "[your_environment_id]"
headers = {
    'accept': "application/json",
    'x-api-key': "your_api_key",
    'content-type': "application/json",
    'cache-control': "no-cache"
    }

response = requests.request("POST", url, data=payload, headers=headers)

print(response.text)
