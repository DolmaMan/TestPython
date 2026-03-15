import typing
import string
from collections import Counter

def render(template:str, context, placeholder = '$'):
    class CustomTemplate(string.Template):
        delimiter = placeholder

    custom_template = CustomTemplate(template)
    # text = custom_template.substitute(context)
    text = custom_template.safe_substitute(context)
    return text

# Я люблю программирование  -> 'Я', '', ''
def analyze(text):
    print("Идёт удаление пунктуации и разбиение текста на отдельные слова")
    words = text.translate(str.maketrans('', '', string.punctuation)).lower().split()
    print(words)
    print("Удаление слов, которые не вносят вклад в контекст...")
    filter_words = [word for word in words if len(word) > 3]
    print(filter_words)
    print("Подсчёт вхождений для каждого слова...")
    counts = Counter(filter_words)
    print(counts)
    common_word = counts.most_common(1)[0][0] if counts else "call to administrator"
    print(f"Наиболее популярное слово: '{common_word}'")
    return common_word

def choice_template(context):
    if not context ==  "call to administrator":
        print("Контекст успешно определён. Использую шаблон")
    else:
        print("Перенаправляю на администратора")

text = "Вы можете искать решение проблемы за рабочим столом, но в реальности решение приходит в самые неожиданные моменты: за рулём, на пробежке, в душе или во время просмотра фильма. Вдруг, среди обычных мыслей, всплывает решение сложной ошибки или архитектурное решение. И нет, это не миф – любой разработчик подтвердит, что мозг продолжает работать над задачей даже в фоновом режиме.Этот эффект – одновременно дар и проклятие. С одной стороны, постоянный рост и развитие, новые вызовы и чувство удовлетворения от найденного решения. С другой – сложность отключиться, возможность «застрять» в проблеме даже в выходные и во время отдыха."
false_text = "  "

common_context = analyze(text)
choice_template(common_context)

common_failed_context = analyze(false_text)
choice_template(common_failed_context)

# template = "Hello, $name. Nice to $work with. Your balance is $balance"
# context= {'name':'Alice',
#            'balance': 1000}
#
# result = render(template, context)
# print(result)