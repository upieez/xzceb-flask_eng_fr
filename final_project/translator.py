"""language service provided by ibm"""
from ibm_watson import LanguageTranslatorV3

translator = LanguageTranslatorV3(version="2018-05-01")

class MachineTranslation():
    """the start of it all"""
    def english_to_french(self):
        """Takes in a word and uses IBM method to transform to fr"""
        result = translator.translate(text=[self], model_id="en-fr").get_result()
        return result['translations'][0]['translation']
    def french_to_english(self):
        """ Takes in a word """
        result = translator.translate(text=[self], model_id="fr-en").get_result()
        return result['translations'][0]['translation']
