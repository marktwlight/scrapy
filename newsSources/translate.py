from googletrans import Translator
# from googletrans.exceptions import TimeoutException

# from googletrans import exceptions

def translate_text(text, target_language='pt'):
    try:
        translator = Translator()
        translation = translator.translate(text, dest=target_language)
        return translation.text
    except Exception:
        print("Translation timed out")
        return None
