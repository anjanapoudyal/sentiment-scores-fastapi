
from src.happy_ts import HappyTs
from src.lab_mt import LabMt
from src.tokenize import Tokenize
from src.vader import SsVader
import json
from fastapi import FastAPI


app = FastAPI()

# @app.get("/")

# def root():
# return{'Hello': 'World'}
vader = SsVader()
happy_ts = HappyTs()
lab_mt = LabMt()

@app.get('/sentiment-score')
def sentiment_api(text: str, model_name: str):
    if model_name == "VADER":
        return vader.score(text)
    elif model_name == "HAPPY_TC":
        return happy_ts.score(text)
    elif model_name == 'LAB_MT':
        return lab_mt.score(text)
    else:
        print("Invalid model_name")    





tokenize = Tokenize()
@app.get("/tokenize")
def tokenize_api(text: str, token_type: str):

    if token_type == "Words":
        return tokenize.words(text)
    elif token_type == "Sentences":
        return tokenize.sentences(text)
    else:
        print("Invalid token")


