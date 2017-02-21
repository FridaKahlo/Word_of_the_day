import requests, json
def main():
    jum_de_url = half_url_image()
    url_image = whole_url(jum_de_url)
    image = save_image(url_image)

def half_url_image():
    response = requests.request('GET','http://www.bing.com/HPImageArchive.aspx?format=js&idx=0&n=1&mkt=en-US')
    response_json = response.json()
    print(response_json)

    url_image = response_json['images'][0]['url']
    print(url_image)
    return url_image

def whole_url(jum_de_url):
    first_half_url= 'http://www.bing.com/'
    whole_url = first_half_url+jum_de_url
    print (whole_url)
    return whole_url

def save_image(url_image):
    response = requests.get(url_image)
    image_data = response.content
    f = open('D:/Programming/Word_of_the_day/image.jpg','wb')
    f.write(image_data)
    f.close()


if __name__ == '__main__':
    main()