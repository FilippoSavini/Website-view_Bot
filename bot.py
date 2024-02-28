import time
from selenium import webdriver
from selenium.webdriver.common.by import By


def visit_website(url):
    try:
        driver = webdriver.Chrome()
        driver.get(url)
        time.sleep(5)
        search_box = driver.find_element(by = By.NAME, value='q')
        search_box.send_keys("Agriturismo Ben Ti Voglio")
        search_box.submit()
        # Find the "Images" link
        site_link = driver.find_element(by=By.PARTIAL_LINK_TEXT, value="Agriturismo Ben Ti Voglio - Official Website")
        # Click on the "Images" link
        site_link.click()
        # Wait for the page to load
        time.sleep(5)
        print(f"Successfully visited {url}")
        driver.quit()
    except Exception as e:
        print(f"An error occurred while visiting {url}: {e}")
        

if __name__ == "__main__":
    website_url = "http://www.google.com/"  # Replace with the URL of the website you want to visit
    while True:
        visit_website(website_url)
        break