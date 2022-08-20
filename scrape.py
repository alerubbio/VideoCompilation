from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from time import sleep
import json

# webdriver PATH
service = Service(executable_path="E:\Projects\TwitchMontage\VideoCompilation\chromedriver.exe")

# twitch login
USERNAME = ''
PASSWORD = 'bungeeportfolio2099'

# change webdriver download preferences
DOWNLOAD_FILE_PATH = 'E:\Projects\TwitchMontage\VideoCompilation\VideoFiles\\raw_clips'
chrome_options = webdriver.ChromeOptions()
prefs = {'download.default_directory' : DOWNLOAD_FILE_PATH}
chrome_options.add_experimental_option('prefs', prefs)

# open driver instance and desired window
DRIVER_INIT_LINK = 'https://www.twitch.tv/directory/game/VALORANT/clips?range=7d'
driver = webdriver.Chrome(service=service, options=chrome_options)
driver.implicitly_wait(5)
driver.get(DRIVER_INIT_LINK)

# xpath can search for raw text
driver.find_element("xpath", '//*[text()="Language"]').click()
driver.find_element("xpath", '//*[text()="English"]').click()

DESIRED_NUMBER_OF_CLIPS = 60

def get_refs():

    # //a[@data-a-target='preview-card-image-link']
    # // means node, first a is anchor tag, @ lets you specify the 'data-a-target' attribute with a value
    
    # gets 20 clips per 'count'
    count = 0
    while count < 3:
        refs = driver.find_elements("xpath", "//a[@data-a-target='preview-card-image-link']")
        driver.execute_script("arguments[0].scrollIntoView(true);", refs[-1])

        # wait for the page to update
        sleep(1)
        count += 1

    return refs

# downloads clips to folder and creates JSON containing metadata for each video downloaded
def handle_refs():
    refs = get_refs(driver)
    print("reference length after: " + str(len(refs)))

    # open all tabs with clips
    action = ActionChains(driver)
    original_window = driver.current_window_handle

    counter = 0
    for ref in refs:
        if counter == DESIRED_NUMBER_OF_CLIPS:
            break
        action.key_down(Keys.CONTROL).click(ref).key_up(Keys.CONTROL).perform()
        counter += 1

    clips = {}

    # loop through tabs, downloads video and gathers metadata
    for count, window_handle in enumerate(driver.window_handles):
        if window_handle != original_window:
            driver.switch_to.window(window_handle)
            sleep(1)

            # get the video link 
            srcLink = driver.find_element("tag name", "video").get_attribute('src')
            driver.get(srcLink)
            sleep(1)

            streamTitle = driver.find_element("xpath", "//h2[@data-a-target='stream-title']").get_attribute('title')

            fileName = "clip" + str(len(refs) - count) + ".mp4"
            clip_data = {"fileName": fileName, "srcLink": srcLink, "streamTitle": streamTitle }
            clips.append(clip_data)

            driver.close()

    return clips

# ends the scrape.py webdriver session
# driver.close()

# TODO:
# - Add scrolling in case we need more clips
# - Scrape other metadata for video description 