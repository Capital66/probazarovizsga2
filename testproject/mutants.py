from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import NoSuchElementException
import time

driver = webdriver.Chrome(ChromeDriverManager().install())

# weblap megkeresése
driver.get("https://witty-hill-0acfceb03.azurestaticapps.net/mutant_teams.html")
time.sleep(3)

# Original X-Men csoport kiválasztása
original = driver.find_element_by_xpath('/html/body/div/label[1]').click

iceman = driver.find_element_by_id('iceman')
time.sleep(3)

# X-Factor csoport kiválasztása
x_factor = driver.find_element_by_xpath('/html/body/div/label[3]').click