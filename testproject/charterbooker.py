from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import NoSuchElementException
import time
from selenium.webdriver.support.ui import Select

driver = webdriver.Chrome(ChromeDriverManager().install())

# weblap megkeresése
driver.get("https://witty-hill-0acfceb03.azurestaticapps.net/charterbooker.html")
time.sleep(3)

# TC01 Nincs kiválasztva vendégszám
button_next = driver.find_element_by_xpath('//*[@id="step1"]/ul/li[2]/button')
button_next.click()
assert driver.find_element_by_id('bf_totalGuests-error').text == str.upper('This field is required.')

# TC02 2 vendég kiválasztása
select_item = Select(driver.find_element_by_xpath('//*[@id="step1"]/ul/li[1]/select'))
select_item.select_by_visible_text('2')
time.sleep(3)
button_next.click()

# Foglalási adatok megadása
driver.find_element_by_name('bf_date').send_keys('2021-08-01')
Select(driver.find_element_by_name('bf_time')).select_by_visible_text('Morning')
Select(driver.find_element_by_name('bf_hours')).select_by_visible_text('8')
time.sleep(3)
driver.find_element_by_xpath('//*[@id="step2"]/ul/li[4]/button').click()

# Személyes adatok megadása
driver.find_element_by_name('bf_fullname').send_keys('Leo Roberts')
driver.find_element_by_name('bf_email').send_keys('leoroberts@gmail.com')
driver.find_element_by_xpath('//*[@id="step3"]/ul/li[4]/button').click()
time.sleep(3)

# Válasz ellenőrzése
assert driver.find_element_by_xpath(
    '//*[@id="booking-form"]/h2').text == "Your message was sent successfully. Thanks! We'll be in touch as soon as we can, which is usually like lightning (Unless we're sailing or eating tacos!)."
