# task 5.1.

input_data = dict(first_name="Alyssa", last_name="Beaver", email="walch_a@yahoo.com", age=34)


# input_data = dict(first_name="Elvis", last_name="Presley", email="elvis_live@gmail.com", age=42)
# input_data = dict(first_name="Kristen", last_name="Stewart", email="c_st@gmail.com", age=26)


list_clean = []
list_value = input_data.values()
a = None
for value in list_value:
    if type(value) == str and len(value) > 5:
        if value.find("a") != -1:
            list_clean.append(value)
    else:
        if type(value) == int and 25 < value < 40:
            a = value
for x in list_clean:
    if x.rfind("n") != -1 or x.rfind("m") != -1:
            list_clean.remove(x)
list_clean.sort(reverse=True)
list_clean.append(str(a))
print(list_clean)
str_value = ','.join(list_clean)
list_result = str_value.split(',')
print(str_value)
print(list_result)
