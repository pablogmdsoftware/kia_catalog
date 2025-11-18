from selenium import webdriver
from time import sleep

class GetDriver():
    def __init__(self):
        self.driver = webdriver.Firefox()
    def __enter__(self):
        return self.driver
    def __exit__(self,exc_type,exc_value,exc_traceback):
        self.driver.close()

with GetDriver() as driver:
    driver.get("https://www.parts-catalogs.com/eu/demo#/catalogs?catalogId=kia")
    sleep(1)

