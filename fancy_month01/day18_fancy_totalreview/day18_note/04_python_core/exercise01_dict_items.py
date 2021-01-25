dict01 = {'金海': 30, '徐天': 15, '田丹': 0, '柳如思': 500, '铁林': 20}


# list_dict01 = list(dict01.items())
# print(list_dict01)

def condition():
    pass


def dict_ascending(dictx):
    list_dict = list(dictx.items())
    for i in range(0, len(list_dict)):
        for r in range(i + 1, len(list_dict)):
            if list_dict[i][1] > list_dict[r][1]:
                list_dict[i], list_dict[r] = list_dict[r], list_dict[i]
    return dict(list_dict)


# 草稿
# for i in range(0, len(list_dict01)):
#     for r in range(i + 1, len(list_dict01)):
#         if list_dict01[i][1] > list_dict01[r][1]:
#             list_dict01[i], list_dict01[r] = list_dict01[r], list_dict01[i]
#
# print(list_dict01)
# dict01 = dict(list_dict01)
# print(dict01)

print(dict_ascending(dict01))
