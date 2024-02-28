import time
from selenium.webdriver.common.by import By
from selenium import webdriver



driver = webdriver.Chrome()  # Optional argument, if not specified will search path.

driver.get('http://www.google.com/')

time.sleep(5) # Let the user actually see something!

search_box = driver.find_element(by = By.NAME, value='q')


search_box.send_keys('Agriturismo Ben Ti Voglio')

search_box.submit()

time.sleep(5) # Let the user actually see something!

driver.quit()