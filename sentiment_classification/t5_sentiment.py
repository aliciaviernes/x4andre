"""
  https://huggingface.co/mrm8488/t5-base-finetuned-imdb-sentiment
"""

from transformers import AutoTokenizer, AutoModelWithLMHead

model_path = "mrm8488/t5-base-finetuned-imdb-sentiment"
tokenizer = AutoTokenizer.from_pretrained(model_path)
model = AutoModelWithLMHead.from_pretrained(model_path)

def get_t5_sentiment(text):
  input_ids = tokenizer.encode(text + '</s>', return_tensors='pt')

  output = model.generate(input_ids=input_ids,
                          max_length=2)
  
  dec = [tokenizer.decode(ids) for ids in output]
  label = dec[0]
  return label


if __name__ == "__main__":  
  
  sent = get_t5_sentiment("I dislike a lot that film")
  print(sent)

  # Output: 'negative'
