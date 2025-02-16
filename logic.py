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

    def __init__(self, text, owner):
        self.text = text
        self.owner = owner
        self.translation = self.__translate(self.text, "ru", "en")
        self.response = self.get_answer()
        TextAnalysis.memory[self.owner].append(self)
    # Задание №1

    def __init__(self, text, owner):

        # Задание №2
        TextAnalysis.memory[owner]. append(self)
    def get_answer(self):
        res = self.translate("I don't know how to help", "en", "ru") 
        return res

    def __translate(elf, text, from_lang, to_lang) :
        try:
            translator = Translator(from_lang, to_lang)
            translated_text = translator.translate(text)
            return translated_text
        except Exception as e:
            print(f"Error during translation:{e}")
            return "Перевод не удался"

