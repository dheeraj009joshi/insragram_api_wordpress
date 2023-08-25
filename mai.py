import requests

url = 'https://api.lamadava.com/s1/direct/send'
access_token = 'CFtr2422gV9MyO0g9tj9KPz2jhJNZmau'

# Parameters
params = {
    'user_ids': '60192046661,53212895823,61218778196,39421496660,9067460703,60492581216,15869750369,51249250173,48364835200,60880617611',
    'sessionid': '60766907076%3A3qG91EMjuYCpbM%3A17%3AAYc6Dzj2NhU5lxv10P82-HcnaOj_qIhteKjfClQklg',
    'text': 'this is text',
    'access_key':'CFtr2422gV9MyO0g9tj9KPz2jhJNZmau'
}

# Headers
headers = {
    'accept': 'application/json',
    'Content-Type': 'application/x-www-form-urlencoded',
    'access_key': 'CFtr2422gV9MyO0g9tj9KPz2jhJNZmau'
}

# Make the POST request
response = requests.post(url, data=params, headers=headers)

# Check the response
if response.status_code == 200:
    print("Request successful!")
    print(response.json())
else:
    print("Request failed!")
    print(f"Status Code: {response.status_code}")
    print(response.text)
