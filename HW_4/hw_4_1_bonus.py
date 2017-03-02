# bonus 4.1
print("TASK 1&2" + "\n")
a = [25, False, "124", ["c:", "Program files"], {'Shakhtar': 'Donetsk', 'Dynamo': 'Kiev'}]

# variant 1
print("variant 1")
print(a[0])
print(a[1])
print(a[2])
print(a[3])
print(a[4])
# print(a[6]) index is nothing, thet because error
print('\n')

# variant 2


print("variant 2")
for x in a:
    print(x)
print('\n')

# variant 3


print("variant 3")
i = len(a)
j = 0
while j <= i - 1:
    print(a[j])
    j += 1
print('\n')


"""
3. Превратить строку "123.456" в число и число с плавающей точкой.
4. Превратить число 93735 сначало в число с плавающей точкой, а затем в строку.
"""
print("TASK 3&4" + "\n")
c = "123.456"
d = 93735
print(float(c))
e = float(d)
print(e)
print('"' + str(e) + '"')
