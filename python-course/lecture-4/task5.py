my_list = ["2018-01-01", "yandex", "cpc", 100]
result = my_list[-1]
del my_list[-1]
for key in reversed(my_list):
    result = {key: result}
print(result)
