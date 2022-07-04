import os
from selenium.webdriver import Chrome
from selenium.webdriver import Firefox

HOST = 'https://demoqa.com'
LOGIN = os.environ['LOGIN']
PASSWORD = os.environ['PASSWORD']

AUTOMATION_PRACTICE_HOST = 'http://automationpractice.com/'
DRIVER = Firefox()
WAIT_TIME = 30
