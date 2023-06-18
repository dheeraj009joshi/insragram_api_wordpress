






import requests
r = requests.post(
    "https://api.deepai.org/api/text2img",
    data={
        'text': 'an yellow monkey eating banana on a black rock ',
        'grid_size':1
    },
    headers={'api-key': 'quickstart-QUdJIGlzIGNvbWluZy4uLi4K'}
)
print(r.json())