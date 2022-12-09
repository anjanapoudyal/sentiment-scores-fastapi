import flair
from flair.data import Sentence



class FLairNLP:
    def __init__(self):
        self.classifier = flair.models.TextClassifier.load('en-sentiment')
       
        

    def score(self, text):
        sentence = Sentence(text)
        result= self.classifier.predict(sentence)
        return result
    
