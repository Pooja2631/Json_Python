# my_dict = {'4': 5, '6': 7, '1': 3, '2': 4}
# sorted_dict = my_dict.keys()
# sorted_dict = sorted(sorted_dict)
# print("Sorted dictionary using sorted() and keys() is : ")
# for key in sorted_dict:
#     print(key,':', my_dict[key])


import json
a={
    '4': 5, 
    '6': 7, 
    '1': 3, 
    '2': 4}
print(json.dumps(a,indent=4,sort_keys=True))