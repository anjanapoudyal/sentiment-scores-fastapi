
from happytransformer import HappyTextClassification


class HappyTs:
    def __init__(self):
        self.analyser = HappyTextClassification(
            model_type="DISTILBERT",  model_name="distilbert-base-uncased-finetuned-sst-2-english",num_labels=2)

    def score(self, text):

        result = self.analyser.classify_text(text)
        return result
    
    