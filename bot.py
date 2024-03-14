import time
from selenium import webdriver
from selenium.webdriver.common.by import By


def visit_website(url):
    try:
        # Setup the Chrome options to start maximized
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("--start-maximized")
        chrome_options.add_argument("--headless")  # Run in headless mode (without opening browser window)
        
        
        # Initialize the Chrome driver with the configured options
        driver = webdriver.Chrome(options=chrome_options)
        
        driver.get(url)
        time.sleep(5)
        
        # Find the website
        search_box = driver.find_element(by = By.NAME, value='q')
        search_box.send_keys("What to search")
        search_box.submit()
        
        # Find the website link
        site_link = driver.find_element(by=By.PARTIAL_LINK_TEXT, value="Website name")
        site_link.click()
        
        # Wait for the page to load
        time.sleep(5)
        
        # Realize one action
        chi_siamo_link = driver.find_element(By.XPATH, "//a[contains(text(), 'Chi siamo')]")
        chi_siamo_link.click()
        time.sleep(10)
        
        print(f"Successfully visited {url}")
        driver.quit()
    except Exception as e:
        print(f"An error occurred while visiting {url}: {e}")
        

if __name__ == "__main__":
    website_url = "http://www.google.com/"  # Replace with the URL of the website you want to visit
    while True:
        visit_website(website_url)
        break