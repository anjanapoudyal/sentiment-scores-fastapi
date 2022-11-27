import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
nltk.download("vader_lexicon")


class SsVader:
    def __init__(self):
        self.analyzer = SentimentIntensityAnalyzer()

    def score(self, text):
        sentiment_dict = self.analyzer.polarity_scores(text)
        compound_var = sentiment_dict["compound"]
        if compound_var > 0:
            return {
                "label": "POSITIVE",
                "score": compound_var
            }
        elif compound_var < 0:
            return {
                "label": "NEGATIVE",
                "score": compound_var}
        else:
            return {
                "label": "NEUTRAL",
                "score": compound_var}
