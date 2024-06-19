import pandas as pd

from pysentimiento import sentiment_pipeline
from t5_sentiment import get_t5_sentiment


def triple_sentiment_analysis(input_list, output_path):
    # Input should be a list of strings (sentences)
    # Output should be the correct path to a CSV file.
    
    future_dataframe = list()
    
    for tweet in input_list:
        row = list()
        row.append(tweet)
        row.append(sentiment_pipeline(tweet))
        row.append(sentiment_pipeline(tweet, mode='roberta'))
        row.append(get_t5_sentiment(tweet))
        future_dataframe.append(row)

    df = pd.DataFrame(future_dataframe, columns=['tweet', 'bert', 'roberta', 't5'])
    df.to_csv(output_path)


if __name__ == "__main__":
    examples = [
                "I adore this weather",  # should be positive
                "This weather is okay, I don't have feelings about it",  # should be neutral 
                "My guts hate this weather",  # should be negative
            ]
    triple_sentiment_analysis(input_list=examples,
                              output_path="out.csv")
