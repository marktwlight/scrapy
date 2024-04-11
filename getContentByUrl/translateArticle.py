from googletrans import Translator
# from googletrans.exceptions import TimeoutException

# from googletrans import exceptions
# pip install googletrans == 3.1.0a0


def tranlate_to_english(text, target_language='en'):
    try:
        translator = Translator()
        translation = translator.translate(text, dest=target_language)
        return translation.text
    except Exception:
        print("Translation timed out")
        return None


def translate_text(text, target_language='pt'):

    try:
        content = tranlate_to_english(text)
        translator = Translator()
        translation = translator.translate(content, dest=target_language)
        return translation.text
    except Exception:
        print("Translation timed out")
        return None


# 先翻译成英语，再翻译成葡语
# result = translate_text("hello world")
# print(result)
