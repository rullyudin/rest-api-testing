import requests
import json
import pandas as pd

response = requests.get('https://api.stackexchange.com/2.3/questions?order=desc&sort=activity&site=stackoverflow')

print(pd.DataFrame(response.json()).head())
print(response.json()['items'])

for data in response.json()['items']:
    if data['answer_count'] == 0:
        print(data['title'])
        print(data['link'])
    else:
        pass
    print()