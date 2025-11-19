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

def extract_headers(driver,class_name="a05Das4P-N8-"):
    wait = WebDriverWait(driver, 10)
    row = wait.until(EC.presence_of_element_located((By.CLASS_NAME,class_name)))
    th_list = row.find_elements(By.TAG_NAME, "th")
    headers = []
    for th in th_list:
        headers.append(th.text)
    return headers

def extract_information(
    row,
    info_button_class = "OU86QPYRbD0-",
    modal = "ELkpm5Bw0qE-",
    modal_text = "k0mox4rl57k-",
    close_button_class = "CMTDFscG6Hw-",
):

    td_list = row.find_elements(By.TAG_NAME, "td")

    values = []

    for td in td_list:
        values.append(td.text)

    time.sleep(1)

    info_button = row.find_element(By.CLASS_NAME,info_button_class)
    info_button.click()

    modal = wait.until(EC.visibility_of_element_located((By.CLASS_NAME,modal)))

    modal_text = modal.find_element(By.CLASS_NAME,modal_text).text

    time.sleep(1)

    close_button = modal.find_element(By.CLASS_NAME,close_button_class)
    close_button.click()

    time.sleep(1)

    return {"row": 0, "row_text": values, "info": modal_text}

def split_information_text(text):
    text.split("\n;")
    text_dict = {}
    for column in text.split(";\n"):
        if column.find(":") > 0:
            column_tuple = column.split(": ")
            text_dict[column_tuple[0]] = column_tuple[1]
        else:
            text_dict["#"] = column
    return text_dict

with GetDriver() as driver:
    driver.get("https://www.parts-catalogs.com/eu/demo#/models?catalogId=kia&modelId=39e5d73321b21fceafd48d9e04dc8b66&transmission=01265cbeececa6d105180f9f3ad13cc1")
    wait = WebDriverWait(driver, 10)

    time.sleep(1)

    # click_load_buttons(driver)

    # time.sleep(1)

    tbody = extract_tbody(driver)

    time.sleep(1)

    rows = extract_rows(tbody)

    print(len(rows))

    row = rows[0]

    # print(row)
    # print(row.text)

    time.sleep(1)

    information = extract_information(row)

    print(split_information_text(information.get("info")))

    print(information)

    print(extract_headers(driver))

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


