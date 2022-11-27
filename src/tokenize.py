import nltk
nltk.download('punkt')

class Tokenize:
    
    def __init__(self) :
        pass
    def sentences(self,text):
        tokens_sent = nltk.sent_tokenize(text)
        return tokens_sent 
    
    def words(self,text):
        tokens_word = nltk.word_tokenize(text)
        return tokens_word