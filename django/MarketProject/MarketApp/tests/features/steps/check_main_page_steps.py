from selenium.webdriver.support import expected_conditions as cond
from selenium.webdriver.common.by import By

@given('Main Market Page To Check')
def step(context):
    context.browser.get('http://127.0.0.1:8000/')

@then('Check Number of Supermarkets')
def step(context):
    number_of_supermarkets = 6
    supermarket_div = "col-lg-3.col-md-6.mb-4"
    context.wait.until(cond.element_to_be_clickable((By.CLASS_NAME, supermarket_div)))
    supermarkets = context.browser.find_elements_by_class_name(supermarket_div)
    assert len(supermarkets) == number_of_supermarkets