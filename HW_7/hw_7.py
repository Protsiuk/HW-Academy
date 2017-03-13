# Homework 7

from datetime import datetime, timedelta
import logging
from argparse import ArgumentParser

parser = ArgumentParser()
parser.add_argument("-l", "--level", dest="level_logging", choices=["DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"],
                    help="input level_logging")
args = parser.parse_args()
loglevel = getattr(logging, str(args), None)
logging.basicConfig(filename='logs.log', format='%(asctime)s %(message)s', filemode='w',
                    datefmt='%m/%d/%y %I:%M %p', level=loglevel)
date_format = "%Y-%m-%d"
now = datetime.now()
best_friend_birthday = input("Input your friend's Birthday YYYY-MM-DD: ")

datetime_best_friend_birthday = datetime.strptime(best_friend_birthday, date_format)
timedelta_range = now + timedelta(days=7)
if type(datetime_best_friend_birthday) == datetime:
    logging.info("input data was correct.")
else:
    logging.error("wrong input data.")
if now.date() < datetime_best_friend_birthday.date() <= timedelta_range.date():
    print("Your friend's birthday will be next week.")
    logging.warning("Need a gift")
else:
    print("Don't worry! You have a time to prepare of gift for your friend.")
    logging.info("Birthday it will not be soon")
