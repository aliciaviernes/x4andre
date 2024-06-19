"""
    https://huggingface.co/cardiffnlp/twitter-roberta-base-sentiment-latest
"""

# from transformers import pipeline
# sentiment_task = pipeline("sentiment-analysis", model=model_path, tokenizer=model_path)
# sent = sentiment_task("Covid cases are increasing fast!")
# print(sent)

from transformers import AutoModelForSequenceClassification
from transformers import TFAutoModelForSequenceClassification
from transformers import AutoTokenizer, AutoConfig
import numpy as np
from scipy.special import softmax

# Preprocess text (username and link placeholders)
def preprocess(text):
    new_text = []
    for t in text.split(" "):
        t = '@user' if t.startswith('@') and len(t) > 1 else t
        t = 'http' if t.startswith('http') else t
        new_text.append(t)
    return " ".join(new_text)

MODEL = f"cardiffnlp/twitter-roberta-base-sentiment-latest"

tokenizer = AutoTokenizer.from_pretrained(MODEL)
config = AutoConfig.from_pretrained(MODEL)
# PT
model = AutoModelForSequenceClassification.from_pretrained(MODEL)

#model.save_pretrained(MODEL)

def roberta_twitter(text):
    
    text = preprocess(text)
    encoded_input = tokenizer(text, return_tensors='pt')
    output = model(**encoded_input)
    scores = output[0][0].detach().numpy()
    scores = softmax(scores)
    # # TF
    # model = TFAutoModelForSequenceClassification.from_pretrained(MODEL)
    # model.save_pretrained(MODEL)
    # text = "Covid cases are increasing fast!"
    # encoded_input = tokenizer(text, return_tensors='tf')
    # output = model(encoded_input)
    # scores = output[0][0].numpy()
    # scores = softmax(scores)
    # Print labels and scores
    ranking = np.argsort(scores)
    ranking = ranking[::-1]
    labels = list()
    for i in range(scores.shape[0]):
        l = config.id2label[ranking[i]]
        labels.append(l)
    return labels[0]
        # l = config.id2label[ranking[i]]
        # s = scores[ranking[i]]
        # print(f"{i+1}) {l} {np.round(float(s), 4)}")

if __name__ == "__main__":
    sent = roberta_twitter("Covid cases are increasing fast!")
    print(sent)
