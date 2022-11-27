

from labMTsimple.storyLab import *
from labMTsimple.speedy import *


class LabMt:
    def __init__(self):
        lang = 'English'
        self.labMT, self.labMTvector, self.labMTwordList = emotionFileReader(
            stopval=0.0, lang=lang, returnVector=True)

    def score(self, text):

        Valence, fvec = emotion(text, self.labMT, shift=True,
                                happsList=self.labMTvector)
        StoppedVec = stopper(fvec, self.labMTvector,
                             self.labMTwordList, stopVal=1.0)

        Happiness_score = emotionV(StoppedVec, self.labMTvector)
        if Happiness_score > 5:
            return {
                "label": "POSITIVE",
                "score": Happiness_score
            }
        elif Happiness_score < 5:
            return {
                "label": "NEGATIVE",
                "score": Happiness_score}
        else:
            return {
                "label": "NEUTRAL",
                "score": Happiness_score}
