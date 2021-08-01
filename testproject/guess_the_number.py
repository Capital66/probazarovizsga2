from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import NoSuchElementException
import time

driver = webdriver.Chrome(ChromeDriverManager().install())

# weblap megkeresése
driver.get("https://witty-hill-0acfceb03.azurestaticapps.net/guess_the_number.html")
time.sleep(3)

# Tipp megadása
for i in range(101):
    tip = driver.find_element_by_xpath('/html/body/div/div[2]/input')
    tip.send_keys(i)
    button_guess = driver.find_element_by_xpath('/html/body/div/div[2]/span/button')
    button_guess.click()
    tip.clear()
