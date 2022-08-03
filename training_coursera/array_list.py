
# list1 = [1, 2, 3, 4]
# list2 = [2, 3, 4]
# list3 = [3, 4, 5]
#
# def get_super_int(list1, list2, list3):
#     super_int = []
#     for i in list1:
#         for b in list2:
#             for c in list3:
#                 if i==b==c:
#                     super_int.append(i)
#
#     return  super_int
#
#
# print(get_super_int(list1, list2, list3))

list = ["a", "bc", "def", "sdw"]

def max_string(list):
    res_str = ""

    for i in list:
        if len(i) > len(res_str):
            res_str = i
    return res_str

print(max_string(list))

print(max(list, key=len))

