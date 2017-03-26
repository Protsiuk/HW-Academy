# Homework 8_Bonus task_8&9
# This is a file was pushed to HW_8 27.03.

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
import csv
import os

chromedriver = os.path.join(os.path.dirname(os.path.abspath(__file__)), "chromedriver")
os.environ["webdriver.chrome.driver"] = chromedriver
driver = webdriver.Chrome(chromedriver)
result = []
driver.get("https://toster.ru/")
questions = driver.find_elements_by_class_name("question_short")

for element in questions:
    question = element.find_element_by_class_name("question__title-link").text
    data_publish = element.find_element_by_class_name("question__date_publish").get_attribute("datetime").split()[0]
    followers = element.find_element_by_class_name("question__views-count").text.split()[0]
    if followers != "нет":
        pass
    else:
        followers = "0"
    number_answers = element.find_element_by_class_name("mini-counter__count_grey").text

# icon check
    try:
        element.find_element_by_class_name("icon_check")
        correct_answer = True
    except NoSuchElementException:
        correct_answer = False

    result.append([question, data_publish, followers, number_answers, correct_answer])

# going to pages(from 1 up to 20)

paginators = driver.find_elements_by_class_name("paginator__item-link")
number_pages = 1
while number_pages < 20:
    try:
        next_click = driver.find_element_by_class_name("next").click()
        number_pages += 1
    except ValueError:
        pass
print("Was opened ", number_pages, "pages")

# size window 414х736

driver.set_window_size(414, 736)

# add to CSV Toster parsing data

with open('torser_parsing.csv', 'w', newline='') as csv_file:
    writer = csv.writer(csv_file)
    writer.writerow(["Question", "Date of public", "Followers", "Number of answers", "Correct answer"])
    for element in result:
        writer.writerow(element)

# bonus task to HW8
driver.get("https://habrahabr.ru")
write_navbar = driver.find_element_by_class_name("btn_navbar_registration").click()
email = driver.find_element_by_xpath("//input[@name='email']").send_keys("sirko@gmail.com")
login = driver.find_element_by_xpath("//input[@name='login']").send_keys("sirko_sobaka")
password = driver.find_element_by_xpath("//input[@name='password']").send_keys("poiuyt")
password2 = driver.find_element_by_xpath("//input[@name='password2']").send_keys("poiuyt")

# Bonus to HW9. Add to CSV "habrahabr" parsing data

with open('habrahabr_parsing.csv', 'w', newline='') as csv_file:
    writer = csv.writer(csv_file)
    writer.writerow(["Email", "Login", "Password", "Repeat password"])
    writer.writerow([email, login, password, password2])

driver.quit()
