import json
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
import os
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']


authenticator = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3(
                        version='2018-05-01',
                        authenticator=authenticator)
language_translator.set_service_url(url)

def englishToFrench(englishText):
    #English to French
    translation = language_translator.translate(
                            text=englishText,model_id='en-fr').get_result()
    frenchText=translation['translations'][0]['translation']
    return frenchText

def frenchToEnglish(frenchText):
    #French to English
    translation = language_translator.translate(text=frenchText,model_id='fr-en').get_result()
    englishText=translation['translations'][0]['translation']
    return englishText

Translate_ENG=("Hello","Chocolate","Wine", "Cheese")
for i in Translate_ENG:
    print(englishToFrench(i))

Translate_FRE=("Bonjour","Chocolat","Vin", "Fromage")
for i in Translate_FRE:
    print(frenchToEnglish(i))

