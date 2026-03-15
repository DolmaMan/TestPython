# dict_p = {
#     "key1": {"k1" : 1, "k2" : 2},
#     "key2": 12,
#     "key3": "value3"
# }
# print(dict_p)
# dict_p.update({
#     "key1": 'value1',
#     "key4": 4
# })
# print(dict_p)

import random

def genRandomDictionary(count:int):
    dictionary = {}
    for i in range(count):
        dictionary['key' + str(random.randint(1, 1000000))] \
            = random.randint(1000, 9999)
    return dictionary

def sortDictionaryByKeys(dictionary: dict):
    keys = list(dictionary.keys())
    keys.sort()

    newDict = {}
    for key in keys:
        newDict[key] = dictionary[key]

    return newDict

def sortDictionaryByValues(dictionary: dict):
    values = list(enumerate(dictionary.values()))

    for i in range(len(values)):
        swapped = False
        for j in range(0, len(values) - i - 1):
            if values[j][1] > values[j + 1][1]:
                values[j], values[j + 1] = values[j + 1], values[j]
                swapped = True
        if not swapped:
            break

    newDict = {}
    keys = list(dictionary.keys())
    for index, value in values:
        newDict[keys[index]] = value

    return newDict


dictionary = genRandomDictionary(100)
print(dictionary)
sortedDict = sortDictionaryByValues(dictionary)
print(sortedDict)