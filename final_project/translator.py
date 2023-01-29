from ibm_watson import language_translator_v3

translator = language_translator_v3.LanguageTranslatorV3(version="2018-05-01")

class MachineTranslation():
    def __init__(self, text):
        self.text = text
    
    def english_to_french(self):
        translate = translator.translate(text=[self], model_id="en-fr")
        return translate.result['translations'][0]['translation']
    
    def french_to_english(self):
        translate = translator.translate(text=[self], model_id="fr-en")
        return translate.result['translations'][0]['translation']