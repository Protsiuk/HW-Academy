
from selenium import webdriver

from selenium.common.exceptions import NoSuchElementException
import os

chromedriver = os.path.join(os.path.dirname(os.path.abspath(__file__)), "chromedriver")

os.environ["webdriver.chrome.driver"] = chromedriver
driver = webdriver.Chrome(chromedriver)

driver.get("https://toster.ru/")
questions = driver.find_elements_by_class_name("question_short")

for element in questions:
    print(element.find_element_by_class_name("question__title-link").text)
    data_publish = element.find_element_by_class_name("question__date_publish").get_attribute("datetime").split()[0]
    print("Date of public -", data_publish)

    followers = element.find_element_by_class_name("question__views-count").text.split()[0]
    if followers != "нет":
        print("Number of followers -", followers)
    else: print("Number of followers -", "0")

    Number_answers = element.find_element_by_class_name("mini-counter__count_grey").text
    print("Number of answers -", Number_answers)

# icon check


    try:
        element.find_element_by_class_name("icon_check")
        correct_answer = True
    except NoSuchElementException:
        correct_answer = False
    print("Correct answers -",correct_answer)

    paginators = driver.find_elements_by_class_name("paginator").text.split()

    print(paginators)


    # size window
    driver.set_window_size(414, 736)

driver.quit()
