# Python Version: 3.10
# Selenium Version: 4.6
# Faker Version: 15.3.1

from selenium import webdriver
from faker import Faker
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from config import Config

fake = Faker()
options = Options()
options.add_experimental_option('detach', True)
driver = webdriver.Chrome(options=options)

# 1. Go to https://www.saucedemo.com/
driver.get(Config.URL)
driver.maximize_window()
driver.implicitly_wait(Config.MAX_TIMEOUT)

# 2. Login using the “standard user” and password.
driver.find_element(By.ID, 'user-name').send_keys(Config.USER_NAME)
driver.find_element(By.ID, 'password').send_keys(Config.PASSWORD)
driver.find_element(By.ID, 'login-button').click()

# 3. Add “Sauce Labs Bike Light” to the cart
driver.find_element(By.ID, 'add-to-cart-sauce-labs-bike-light').click()
PRODUCTS_IN_CART = driver.find_element(By.XPATH, "//span[.='1']").text
assert PRODUCTS_IN_CART == '1'

# 4. Navigate to the Cart and checkout the item. Fill in the following information:
# - First Name
# - Last Name
# - Zip/Postal Code
driver.find_element(By.XPATH, "//a[@class='shopping_cart_link']").click()
driver.find_element(By.ID, 'checkout').click()
NAME = fake.name()
FIRST_NAME, LAST_NAME = tuple(NAME.split())
driver.find_element(By.ID, 'first-name').send_keys(FIRST_NAME)
driver.find_element(By.ID, 'last-name').send_keys(LAST_NAME)
ZIP_CODE = fake.zipcode()
driver.find_element(By.ID, 'postal-code').send_keys(ZIP_CODE)

# 5. Click Continue and Finish.
driver.find_element(By.ID, 'continue').click()
driver.find_element(By.ID, 'finish').click()

# 6. Assert that the item has successfully been ordered/confirmed.
TEXT = driver.find_element(By.XPATH, "//h2[@class='complete-header']").text
assert TEXT == Config.TEXT_ORDER_CONFIRMATION
