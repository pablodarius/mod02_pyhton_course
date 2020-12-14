from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait

def before_all(context):
    driver = webdriver.Chrome()
    context.browser = driver
    context.wait = WebDriverWait(context.browser, timeout=10)

def after_all(context):
    context.browser.quit()