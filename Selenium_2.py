from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
import datetime

driver = webdriver.Chrome()
driver.get('https://google.com')
print(f'Page name {driver.title}')
sleep(1)
button1_accept = driver.find_element('id', 'LA')
button1_accept.click()
sleep(1)
search_field = driver.find_element('name', 'q')
search_field.send_keys('Github toubleshooting')
sleep(1)
search_field.send_keys(Keys. ENTER)
search_button = driver.find_element('name', 'btk')
search_button.submit()
sleep(1)

now = datetime.datetime.now()
filename = now.strftime('screenshot-%d_%m-%S.png')
driver.get_screenshot_as_file('image.png')

driver.quit()
