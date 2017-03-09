# Homework bonus 6

import requests
IP_ADRESS_point = "https://echo.getpostman.com/post"
get_post = requests.post(IP_ADRESS_point, {"test": "hi, people!"})
respons = eval(get_post.text)
print("key-"+"form => value - " + str(respons.get("form")))

