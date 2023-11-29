import requests

def check_status(status_code):
    if status_code == 200:
        print('SUCCESS!')
    elif status_code == 404:
        print('FAILURE!')
    else:
        print('unknown status.')

# urls = ['https://api.github.com/this-api-should-not-exist','https://api.github.com']

# for url in urls:
#     response = requests.get(url)
#     check_status(response.status_code)

# response=requests.get('https://imgs.xkcd.com/comics/making_progress.png')
# resp_json = response.json()
# for k in resp_json.keys():
#     print(k)

# with open(r'img.png','wb') as f:
#     f.write(response.content)

pload = {'username':'Olivia','password':'123'}
response = requests.post('https://httpbin.org/post', data = pload)
check_status(response.status_code)