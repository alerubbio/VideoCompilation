import pyautogui
from selenium.webdriver.chrome.service import Service
# import Action chains
from selenium.webdriver.common.action_chains import ActionChains
 
# import KEYS
from selenium.webdriver.common.keys import Keys

from selenium import webdriver


service = Service(executable_path="E:\Projects\TwitchMontage\VideoCompilation\chromedriver.exe")
USERNAME = ''
PASSWORD = 'bungeeportfolio2099'

driver = webdriver.Chrome(service=service)
driver.implicitly_wait(4)
driver.get('https://www.twitch.tv/directory/game/VALORANT/clips?range=7d')

# xpath can search for raw text
driver.find_element("xpath", '//*[text()="Language"]').click()
driver.find_element("xpath", '//*[text()="English"]').click()

# //a[@data-a-target='preview-card-image-link']
# // means node, first a is anchor tag, @ lets you specify the 'data-a-target' attribute with a value
# find_elements is iterable with 20 elements
refs = driver.find_elements("xpath", "//a[@data-a-target='preview-card-image-link']")

# open all tabs with first 20 clips
action = ActionChains(driver)
original_window = driver.current_window_handle

counter = 0
for ref in refs:
    if counter == 3:
        break
    action.key_down(Keys.CONTROL).click(ref).key_up(Keys.CONTROL).perform()
    counter += 1


for window_handle in driver.window_handles:
    if window_handle != original_window:
        driver.switch_to.window(window_handle)
        srcRef = driver.find_element("tag name", "video").get_attribute('src')
        print(srcRef)
        driver.close()
        
        # driver.close()
        
# driver.close()
# driver.quit()