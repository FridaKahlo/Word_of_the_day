import requests, json
import ctypes
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
import logging
import textwrap
log = logging.getLogger("MyLogger")

def main():
    jum_de_url = half_url_image()
    url_image = whole_url(jum_de_url)
    log.debug("Url is retrieved : %s", url_image)
    image_path = save_image(url_image)
    log.debug("Image saved to : %s", image_path)
    quote, author = random_quote()
    formatted_quote = textwrap.fill(quote, 50) + "\n" +author
    path_image_with_text = text_on_image(image_path,formatted_quote,(1200,900),30)
    status = set_wallpaper(path_image_with_text)
    log.debug("Wallpaper set :%s",status)

def random_quote():
    """
    Extract a random quote from brainyquote.com
    :returns: quote and author from a site
    """
    response_quote_page = requests.get('https://www.brainyquote.com/api/rand_q?langc=en')
    response_json_quote_page = response_quote_page.json()
    quote = response_json_quote_page["qt"]
    author = response_json_quote_page["an"]
    return quote, author

def set_wallpaper(image_path):
    """Change the Windows wallpaper to the image given by its path.
    :param image_path: the path of the image that should be set as a wallpaper, e.g. "C:/photos/image.jpg
    :returns: the status code of the ctypes.windll.user32.SystemParametersInfoW function
    """
    SPI_SETDESKWALLPAPER = 20
    result = ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER, 0, image_path, 3)
    return result

def half_url_image():
    """
    :returns: the half url of the image of the day which includes the name of the image
    """
    response = requests.request('GET','http://www.bing.com/HPImageArchive.aspx?format=js&idx=0&n=1&mkt=en-US')
    response_json = response.json()
    log.debug("Type of variable is: %s",type(response_json))
    #print(str(response_json))
    url_image = response_json['images'][0]['url']
    log.debug("URL image: %s",url_image)
    #print(url_image)
    return url_image


def whole_url(jum_de_url):
    """
    :param jum_de_url: the half url of the image of the day which includes the name of the image
    :returns: the whole url of the image of the day
    """
    first_half_url= 'http://www.bing.com/'
    whole_url = first_half_url+jum_de_url
    log.debug("Whole_url: %s",whole_url)
    #print (whole_url)
    return whole_url

def save_image(url_image):
    """
    :param url_image: the whole url of the image of the day
    :returns: the path of the saved image
    """
    response = requests.get(url_image)
    image_data = response.content
    split_url = url_image.split("/")
    log.debug("Split url : %s", split_url)
    #print (type (x))
    name_of_image = split_url[-1]
    #print(z)
    target_path = 'D:/Programming/Word_of_the_day/'+name_of_image
    f = open(target_path,'wb')
    f.write(image_data)
    f.close()
    return target_path

def text_on_image(image_path,formatted_quote,coordinates,size):
    """
    :param image_path: the path of the saved image of the day
    :param formatted_quote: the quote and the author formatted to go to the next line after 50 characters
    :param coordinates: the coordinates (x, y) of the text on the image
    :param size: the size of the text on the image
    :returns path_image_with_text: the path of the image with the quote and author on it
    """
    desen = Image.open(image_path)
    experiment = ImageDraw.Draw(desen)
    font = ImageFont.truetype('calibri.ttf', size)
    experiment.text(coordinates, formatted_quote, (255,0,0),font=font)
    path_image_with_text = 'd:/programming/prived-medved.jpg'
    desen.save(path_image_with_text)
    return path_image_with_text


if __name__ == '__main__':

    logging.basicConfig(filename='D:/Programming/Word_of_the_day/example.log',
                        level=logging.DEBUG,
                        format='%(asctime)s %(levelname)s %(name)s %(message)s',
                        datefmt='%m/%d/%Y %I:%M:%S %p',
                        )
    main()


