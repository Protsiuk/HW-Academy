
from selenium import webdriver

from selenium.common.exceptions import NoSuchElementException
import os

chromedriver = os.path.join(os.path.dirname(os.path.abspath(__file__)), "chromedriver")

os.environ["webdriver.chrome.driver"] = chromedriver
driver = webdriver.Chrome(chromedriver)

driver.get("https://toster.ru/")
questions = driver.find_elements_by_class_name("question_short")


"""

for question in questions:
    print(question.find_element_by_class_name("question__title-link"))
"""

"""
for question in questions:
    print(question.find_element_by_class_name("question__title-link").text)
"""
"""
# number of viewers
for question in questions:
    subscribers = question.find_element_by_class_name("question__views-count").text.split()[0]
    print(subscribers)
"""
"""
# date of public
for question in questions:
    date_public = question.find_element_by_class_name("question__date_publish").get_attribute("datetime")
    print(date_public)
"""
"""
# check icon image
for question in questions:
    try:
        print(question.find_element_by_class_name("icon_check"))
        is_answered = True
    except NoSuchElementExeption:
        is_answered = False
    print(is_answered)
"""
"""
# going to pages
for question in questions:
    try:
        print(question.find_element_by_css_selector("paginator__item"))
        is_pages = True
    except NoSuchElementExeption:
        is_pages = False
    print(is_pages)
"""

# size window
driver.set_window_size(414, 736)


driver.quit()
