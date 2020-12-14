from selenium.webdriver.support import expected_conditions as cond
from selenium.webdriver.common.by import By

@given('Main Market Page')
def step(context):
    context.browser.get('http://127.0.0.1:8000/')

@then('click on checkout button')
def step(context):
    checkout_button = "btn.btn-primary.btn-lg"
    context.wait.until(cond.element_to_be_clickable((By.CLASS_NAME, checkout_button)))
    context.browser.find_element_by_class_name(checkout_button).click()

@then('check the cart price')
def step(context):
    cart_price = "display-4"
    context.wait.until(cond.element_to_be_clickable((By.CLASS_NAME, cart_price)))
    actual_price = context.browser.find_element_by_class_name(cart_price)
    assert "1.99€" in actual_price.text