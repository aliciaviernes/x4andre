# X (formerly Twitter) scraping
Actually pretty easy:
https://medium.com/@vladkens/how-to-still-scrape-millions-of-tweets-in-2023-using-twscrape-97f5d3881434

1. Set up a virtual environment (Python 3.10+)

2. Run:
    1. ```pip install twscrape```
    2. ```twscrape add_accounts accounts.txt username:password:email:email_password``` (the line(s) in the TXT file need to be in this exact format)
    3. ```twscrape login_accounts```

3. ```python main.py``` 

4. If you need to interrupt the loop before completion: run ```python close_loop.py```

Das war's!
