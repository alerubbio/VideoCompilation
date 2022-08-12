import pyautogui
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium import webdriver

# webdriver PATH
service = Service(executable_path="E:\Projects\TwitchMontage\VideoCompilation\chromedriver.exe")

# twitch login
USERNAME = ''
PASSWORD = 'bungeeportfolio2099'

# change webdriver download preferences
DOWNLOADFILEPATH = 'E:\Projects\TwitchMontage\VideoCompilation\VideoFiles\\raw_clips'
chrome_options = webdriver.ChromeOptions()
prefs = {'download.default_directory' : DOWNLOADFILEPATH}
chrome_options.add_experimental_option('prefs', prefs)

# open driver instance and desired window
driver = webdriver.Chrome(service=service, options=chrome_options)
driver.implicitly_wait(5)
driver.get('https://www.twitch.tv/directory/game/VALORANT/clips?range=7d')

# xpath can search for raw text
driver.find_element("xpath", '//*[text()="Language"]').click()
driver.find_element("xpath", '//*[text()="English"]').click()

def get_refs(driver):

    # //a[@data-a-target='preview-card-image-link']
    # // means node, first a is anchor tag, @ lets you specify the 'data-a-target' attribute with a value
    # find_elements is iterable with 20 elements
    
    i = 0
    while i < 2:
        refs = driver.find_elements("xpath", "//a[@data-a-target='preview-card-image-link']")
        driver.execute_script("arguments[0].scrollIntoView(true);", refs[-1])
        print("reference length: " + str(len(refs)))
        i += 1
        
    refs = driver.find_elements("xpath", "//a[@data-a-target='preview-card-image-link']")
    return refs

refs = get_refs(driver)

# open all tabs with clips
action = ActionChains(driver)
original_window = driver.current_window_handle

counter = 0
for ref in refs:
    if counter == 2:
        break
    #action.key_down(Keys.CONTROL).click(ref).key_up(Keys.CONTROL).perform()
    counter += 1


# loop through tabs and download each video
for window_handle in driver.window_handles:
    if window_handle != original_window:
        driver.switch_to.window(window_handle)
        srcLink = driver.find_element("tag name", "video").get_attribute('src')
        driver.get(srcLink)
        driver.close()


# TODO:
# - Add scrolling in case we need more clips
# - Scrape other metadata for video description 