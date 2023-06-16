import requests

url = 'https://api.lamadava.com/a1/media/by/id'
headers = {
    'accept': 'application/json',
    'access-key':"CFtr2422gV9MyO0g9tj9KPz2jhJNZmau"
}
params = {
    'id': '59228183632'
}

response = requests.get(url, headers=headers, params=params)

if response.status_code == 200:
    data = response.json()
    # Process the response data
    print(data)
else:
    print(f'Request failed with status code {response.status_code}')