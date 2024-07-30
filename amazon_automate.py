# Script to log into amazon

from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By


# Ask for email & Password in advance
email = input("Enter ur email: ")
passwd = input("Enter ur passwd: ")

# Firefox Driver
service = Service(GeckoDriverManager().install())

driver = webdriver.Firefox(service=service)
driver.get("https://www.amazon.in/ap/signin?openid.pape.max_auth_age=0&openid.return_to=https%3A%2F%2Fwww.amazon.in%2F%3Fref_%3Dnav_signin&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.assoc_handle=inflex&openid.mode=checkid_setup&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0")

driver.find_element(By.NAME, "email").clear()
driver.find_element(By.NAME, "email").send_keys(email)
driver.find_element(By.CLASS_NAME, "a-button-input").click()

driver.find_element(By.ID, "ap_password").clear()
driver.find_element(By.ID, "ap_password").send_keys(passwd)
driver.find_element(By.ID, "signInSubmit").click()
#driver.close()
