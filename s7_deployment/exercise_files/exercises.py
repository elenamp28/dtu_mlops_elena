import requests

# urls = ['https://api.github.com/this-api-should-not-exist','https://api.github.com']

# for url in urls:
#     response = requests.get(url)
#     if response.status_code == 200:
#         print(f'{url}: SUCCESS!')
#     elif response.status_code == 404:
#         print(f'{url}: FAILURE!')
#     else:
#         print(f'{url}: unknown status.')

response=requests.get('https://imgs.xkcd.com/comics/making_progress.png')
resp_json = response.json()
for k in resp_json.keys():
    print(k)