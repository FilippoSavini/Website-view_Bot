import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

# Richiedi l'URL e il numero di visualizzazioni desiderate
url = input("Inserisci l'URL per generare le visualizzazioni (o lascia vuoto per utilizzare la preimpostazione): ")
if not url:
    url = "http://www.google.com/" # URL preimpostato
try:
    count = int(input("Inserisci il numero di visualizzazioni desiderate: "))
except ValueError:
    print("Devi inserire un numero.")
    exit()

# Imposta le opzioni del WebDriver
options = webdriver.ChromeOptions()
options.add_argument("--incognito")  # Apri la finestra in modalità incognito

# Funzione per attendere il caricamento della pagina
def wait_for_page_load(driver, timeout=7):
    try:
        # Attendere il caricamento dell'elemento body
        WebDriverWait(driver, timeout).until(EC.presence_of_element_located((By.TAG_NAME, "body")))
        return True
    except TimeoutException:
        print("La pagina non si è caricata entro il tempo specificato.")
        return False

# Crea un'istanza del WebDriver
driver = webdriver.Chrome(options=options)

for i in range(count):
    # Apri una nuova scheda
    driver.execute_script("window.open(arguments[0]);", url)
    time.sleep(2)  # Simula l'attesa del caricamento della pagina
    if wait_for_page_load(driver):
        # Se la pagina è stata caricata, chiudi la scheda
        if len(driver.window_handles) > 1:
            driver.switch_to.window(driver.window_handles[-1])
            driver.close()
            driver.switch_to.window(driver.window_handles[0])
    else:
        driver.quit()
        break

# Chiudi il browser dopo aver completato tutte le operazioni
driver.quit()
