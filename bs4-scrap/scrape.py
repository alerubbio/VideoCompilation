##########################################################
#    BEAUTIFUL SOUP WORKS FOR STRAIGHT UP HTML           #
#    SELENIUM IS WHAT YOU NEED FOR JAVASCRIPT SITES      #
#    OR FOR ANY SITES WITH LOTS OF LOADING               #      
##########################################################

from bs4 import BeautifulSoup as bs
import requests
import io

url = "https://www.twitch.tv/directory/game/VALORANT/clips?range=7d"

def get_soup(url):
    return bs(requests.get(url).text, 'html.parser') 

soup = get_soup(url)
for item in soup.select('script'):
    item.extract()

with open("sample.txt", "w", encoding="utf-8") as txt_file:
    txt_file.write(requests.get(url).text)
