# Задание №3
from translate import Translator
import requests
from collections import defaultdict
import requests

# Задание №1
Memory = defaultdict(list)

# Задание №5

class TextAnalysis():   
    memory = defaultdict(list)
    qwestions = {
        "как тебя зовут": "Я супер-крутой-бот и мое предназначение помогать тебе!",
        "сколько тебе лет": "Это слишком философский вопрос",
        "привет": "Здравствуйте!",
        "hello": "Hello!",
        "hi": "Hi!"
    }

    def __init__(self, text, owner):
        self.text = text
        self.owner = owner
        self.translation = self.__translate(self.text, "ru", "en")
        self.response = self.get_answer()
        TextAnalysis.memory[self.owner].append(self)
    # Задание №1

    #def __init__(self, text, owner): #убрал дублирующий __init__

        # Задание №2
        #TextAnalysis.memory[owner]. append(self) #эта строка уже есть в первом __init__
    def get_answer(self):
        # Задание №6
        if self.text.lower() in TextAnalysis.qwestions.keys():
            self.response = TextAnalysis.qwestions[self.text.lower()]
            return self.response
        else:
            res = self.__translate("I don't know how to help", "en", "ru")
            return res

    def __translate(self, text, from_lang, to_lang):
        try:
            translator = Translator(from_lang=from_lang, to_lang=to_lang) #исправил порядок аргументов
            translated_text = translator.translate(text)
            return translated_text
        except Exception as e:
            print(f"Error during translation:{e}")
            return "Перевод не удался"