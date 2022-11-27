import flair
from flair.data import Sentence
from flair.models import TextClassifier


class FLairNLP:
    def __init__(self):
        self.classifier = flair.models.TextClassifier()
       
        

    def score(self, text):
        sentence = Sentence(text)
        result= self.classifier.predict(sentence)
        return result
    
