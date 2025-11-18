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

def extract_tbody(driver,class_name="kTRrWaSE-Eo-"):
    wait = WebDriverWait(driver, 10)
    tbody = wait.until(EC.presence_of_element_located((By.CLASS_NAME,class_name)))
    return tbody

def extract_rows(tbody,class_name="_2agdmOXNL04-"):
    rows = tbody.find_elements(By.CLASS_NAME,class_name)
    return rows

with GetDriver() as driver:
    driver.get("https://www.parts-catalogs.com/eu/demo#/models?catalogId=kia&modelId=bb19fa7c8a2f8ed18ee608f7a14f945d")
    wait = WebDriverWait(driver, 10)

    data = []

    time.sleep(2)

    tbody = extract_tbody(driver)

    time.sleep(2)

    rows = extract_rows(tbody)
    row = rows[0]

    time.sleep(2)

    print(row)
    print(row.text)

    time.sleep(2)

    info_button = row.find_element(By.CLASS_NAME, "OU86QPYRbD0-")
    info_button.click()

    modal = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "ELkpm5Bw0qE-")))

    modal_text = modal.find_element(By.CLASS_NAME, "k0mox4rl57k-").text
    data.append({"row": 0, "info": modal_text})

    time.sleep(1)

    close_button = modal.find_element(By.CLASS_NAME, "CMTDFscG6Hw-")
    close_button.click()

    time.sleep(1)

    # data = []

    # # 3. Loop through rows
    # for i in range(len(rows)):
    #     try:
    #         # Re‑fetch rows each time (DOM may refresh after closing modal)
    #         rows = tbody.find_elements(By.CLASS_NAME, "_2agdmOXNL04-")
    #         row = rows[i]

    #         # Find and click the info button
    #         info_button = row.find_element(By.CLASS_NAME, "OU86QPYRbD0-")
    #         info_button.click()

    #         # Wait for modal to appear
    #         modal = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "CMTDFscG6Hw-")))

    #         # Extract modal text
    #         modal_text = modal.text
    #         data.append({"row": i, "info": modal_text})

    #         # Close modal (click the close button inside modal)
    #         close_button = modal.find_element(By.CLASS_NAME, "CMTDFscG6Hw-")
    #         close_button.click()

    #         # Small pause to avoid race conditions
    #         time.sleep(1)

    #     except Exception as e:
    #         print(f"Error on row {i}: {e}")

print(data[0])


