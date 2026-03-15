from typing import Set, List
from collections import Counter

def split_string(text:str):
    str_list = text.split()
    str_list = list(str_list)
    count = Counter(str_list)
    return count

text = "Георгий Оксана Владимир Вадим Анатолий Оксана Вадим"
result = split_string(text)
print(result)