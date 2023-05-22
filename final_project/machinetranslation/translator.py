'''translator'''
import json
import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']

'''translates text'''
def translate_text(text, model_id):
    authenticator = IAMAuthenticator(apikey)
    language_translator = LanguageTranslatorV3(
        version='2018-05-01',
        authenticator=authenticator
    )
    language_translator.set_service_url(url)

    translation = language_translator.translate(
        text=text,
        model_id=model_id).get_result()

    translated_word = translation['translations'][0]['translation'].split()[0]
    return translated_word

'''English to French'''
def english_to_french(english_text):
    if english_text == None:
        return None
    else:
        model_id = 'en-fr' 
        french_text = translate_text(english_text, model_id)
        return french_text

'''French to English'''
def french_to_english(french_text):
    if french_text == None:
        return None
    else:
        model_id = 'fr-en'
        english_text = translate_text(french_text, model_id)
        return english_text
