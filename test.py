import time
from selenium import webdriver
from selenium.webdriver.common.by import By

def visit_website(url):
    try:
        # Setup the Chrome options to start maximized
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("--start-maximized")
        
        # Initialize the Chrome driver with the configured options
        driver = webdriver.Chrome(options=chrome_options)
        
        # Visit the website
        driver.get(url)
        time.sleep(5)
        
        # Find and click on the "Chi siamo" link
        chi_siamo_link = driver.find_element(By.XPATH, "//a[contains(text(), 'Chi siamo')]")
        chi_siamo_link.click()
        time.sleep(10)

        print(f"Successfully visited {url} and clicked on 'Chi siamo' link.")
        driver.quit()
    except Exception as e:
        print(f"An error occurred while visiting {url}: {e}")

if __name__ == "__main__":
    website_url = "https://agriturismobentivoglio.it/"  # Replace with the URL of the website you want to visit
    while True:
        visit_website(website_url)
        break



