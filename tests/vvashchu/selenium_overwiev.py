from selenium.webdriver import Chrome
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webdriver import WebElement
from selenium.webdriver.common.by import By

HOST = "https://www.saucedemo.com"

session = Chrome().find
session.get(HOST)
