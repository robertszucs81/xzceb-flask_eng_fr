"""
This module contains functions for translating text between English and French.
"""

from deep_translator import MyMemoryTranslator

def english_to_french(english_text):
    """
    Translate the provided text from English to French.
    
    Args:
    english_text (str): Text in English to translate.

    Returns:
    str: Translated text in French.
    """
    try:
        # Create a MyMemoryTranslator instance for English to French
        translator = MyMemoryTranslator(source='english', target='french')

        # Translate the text
        french_text = translator.translate(english_text)

    except Exception as translation_exception:
        # If an error occurs during translation, return the error message
        french_text = str(translation_exception)

    return french_text

def french_to_english(french_text):
    """
    Translate the provided text from French to English.
    
    Args:
    french_text (str): Text in French to translate.

    Returns:
    str: Translated text in English.
    """
    try:
        # Create a MyMemoryTranslator instance for French to English
        translator = MyMemoryTranslator(source='french', target='english')

        # Translate the text
        english_text = translator.translate(french_text)

    except Exception as translation_exception:
        # If an error occurs during translation, return the error message
        english_text = str(translation_exception)

    return english_text
