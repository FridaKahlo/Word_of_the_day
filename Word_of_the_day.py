import requests, json
import ctypes
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

def main():
    jum_de_url = half_url_image()
    url_image = whole_url(jum_de_url)
    image_path = save_image(url_image)
    set_wallpaper(image_path)
    text_on_image(image_path,'test',(700,700),200)

def set_wallpaper(image_path):
    '''Change the Windows wallpaper to the image given by its path.
    :param image_path: str, path to image, e.g. "C:/photos/image.jpg"'''
    SPI_SETDESKWALLPAPER = 20
    result = ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER, 0, image_path, 3)
    return result

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
    x = url_image.split("/")
    print(x)
    #print (type (x))
    z=x[-1]
    print(z)
    target_path = 'D:/Programming/Word_of_the_day/'+z
    f = open(target_path,'wb')
    f.write(image_data)
    f.close()
    return target_path

def text_on_image(image_path,text,coordonates,size):
    desen = Image.open(image_path)
    experiment = ImageDraw.Draw(desen)
    font = ImageFont.truetype('calibri.ttf', size)
    experiment.text(coordonates, text, (255,0,0),font=font)
    desen.save('d:/programming/prived-medved.jpg')


if __name__ == '__main__':
    main()