import time

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_add_to_basket_button_is_on_the_page(browser):
    browser.get(link)
    assert browser.find_element_by_css_selector("#add_to_basket_form > button")
