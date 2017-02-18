import requests, json
response = requests.request('GET','http://www.bing.com/HPImageArchive.aspx?format=js&idx=0&n=1&mkt=en-US')
response_json = response.json()
print(response_json)

url_image = response_json['images'][0]['url']
print(url_image)