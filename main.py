from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, StaleElementReferenceException
from urls import URLS
import time

class GetDriver():
    def __init__(self):
        self.driver = webdriver.Firefox()
    def __enter__(self):
        return self.driver
    def __exit__(self,exc_type,exc_value,exc_traceback):
        self.driver.close()

def click_load_buttons(driver):
    wait = WebDriverWait(driver, 10)
    while True:
        try:
            button = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[contains(@class, 'EH1xtIwTxIU-')]")))
            driver.execute_script("arguments[0].scrollIntoView(true);", button)
            time.sleep(0.2)
            driver.execute_script("arguments[0].click();", button)
            time.sleep(0.7)
        except TimeoutException:
            print("There are no more buttons to click.")
            break

with GetDriver() as driver:
    driver.get("https://www.parts-catalogs.com/eu/demo#/models?catalogId=kia&modelId=1d8274a18f0139854e588412541067fb")
    click_load_buttons(driver)

