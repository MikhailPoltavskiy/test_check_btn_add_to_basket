import time
from selenium.webdriver.common.by import By

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_check_btn_add_to_basket(browser):
    browser.implicitly_wait(10)
    browser.get(link)
    time.sleep(30)
    assert len(browser.find_elements(By.CSS_SELECTOR, "button.btn-add-to-basket")) == 1
