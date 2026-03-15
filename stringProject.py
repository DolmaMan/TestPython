import string
from collections import Counter
import typing

def deleted_punctuation(text:str):
    clean_text = text.translate(str.maketrans('','',string.punctuation))
    print(clean_text)
    words = clean_text.lower().split()
    count = Counter(words)
    return count

def find_popular_words(text:str):
    clean_text = text.translate(str.maketrans('','',string.punctuation)).lower().split()
    print(clean_text)
    filter_words = [word for word in clean_text if len(word) > 3]
    print(filter_words)
    count = Counter(filter_words).most_common(2)
    print(count)
    return count

text = "Вы можете искать решение проблемы за рабочим столом, но в реальности решение приходит в самые неожиданные моменты: за рулём, на пробежке, в душе или во время просмотра фильма. Вдруг, среди обычных мыслей, всплывает решение сложной ошибки или архитектурное решение. И нет, это не миф – любой разработчик подтвердит, что мозг продолжает работать над задачей даже в фоновом режиме.Этот эффект – одновременно дар и проклятие. С одной стороны, постоянный рост и развитие, новые вызовы и чувство удовлетворения от найденного решения. С другой – сложность отключиться, возможность «застрять» в проблеме даже в выходные и во время отдыха."
result = find_popular_words(text)

for word, count in result:
    print(f"Слово '{word}': встречается {count} раз")



