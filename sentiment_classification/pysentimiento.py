"""
    Source: huggingface.com
"""

from transformers import pipeline


def sentiment_pipeline(text, mode='bert'):
    if mode == 'bert':
        model_path = "finiteautomata/bertweet-base-sentiment-analysis"
    elif mode == 'roberta':
        model_path ="cardiffnlp/twitter-roberta-base-sentiment-latest"
    else:
        print("Invalid mode name, choose between bert and roberta.")
    sentiment_task = pipeline("sentiment-analysis", 
                                model=model_path, 
                                tokenizer=model_path)
    return sentiment_task(text)[0]['label']


if __name__ == "__main__":
    sentence = "Covid cases are increasing fast!"
    sent_bert = sentiment_pipeline(sentence)
    print(sent_bert)
    sent_roberta = sentiment_pipeline(sentence, mode='roberta')
    print(sent_roberta)


