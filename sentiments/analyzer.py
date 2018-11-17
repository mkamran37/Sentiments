import nltk

class Analyzer():
    """Implements sentiment analysis."""

    def __init__(self, positives, negatives):
        
        """Initialize Analyzer."""
        self.positives = []
        self.negatives = []
        with open(negatives) as lines:
            for line in lines:
                if not line.startswith(";"):
                    li = line.strip(' \n')
                    self.negatives.append(li)
        with open(positives) as lines:
            for line in lines:
                li = line.strip(' \n')
                if line.startswith(";") == False:
                    self.positives.append(li)

        
    def analyze(self, text):
        tokenizer = nltk.tokenize.TweetTokenizer()
        token = tokenizer.tokenize(text)
        """Analyze text for sentiment, returning its score."""
        score = 0
        for line in token:
            if line.lower() in self.negatives:
                score-=1
            if line.lower() in self.positives:
                score += 1
            else:
                continue
                
        return score
