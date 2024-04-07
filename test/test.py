from googletrans import Translator

def translate_text(text, target_language='pt'):
    translator = Translator()
    translation = translator.translate(text, dest=target_language)
    return translation.text

# Exemplo de uso
english_text = "Hello, how are you?"
portuguese_translation = translate_text(english_text)
print("English:", english_text)
print("Portuguese:", portuguese_translation)