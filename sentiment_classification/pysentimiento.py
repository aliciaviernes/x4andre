"""
    Source: hugginface.com
"""

from transformers import pipeline

# BERT
model_path = "finiteautomata/bertweet-base-sentiment-analysis"

sentiment_task = pipeline("sentiment-analysis", model=model_path, tokenizer=model_path)
sent = sentiment_task("Covid cases are increasing fast!")

print(sent)

# ROBERTA
model_path = f"cardiffnlp/twitter-roberta-base-sentiment-latest"

sentiment_task = pipeline("sentiment-analysis", model=model_path, tokenizer=model_path)
sent = sentiment_task("Covid cases are increasing fast!")

print(sent)
