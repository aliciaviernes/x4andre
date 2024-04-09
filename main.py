import asyncio
import csv
from twscrape import API#, gather
# from twscrape.logger import set_log_level


hashtags = "#leadership #ai"
limit = 5000
output_file = 'leadership_AI_v2.csv'


async def main():
    api = API()
    i = 0
    
    # Option for console printing - would not recommend :)
    # async for tweet in api.search(q, limit=5000):
    #     print(tweet.id, tweet.rawContent)
    
    # Write a CSV file
    async for tweet in api.search(hashtags, limit=limit):
        with open(output_file, 'a', newline='') as csvfile:
            f = csv.writer(csvfile, delimiter=';', quoting=csv.QUOTE_MINIMAL)
            f.writerow([i, tweet.id, tweet.user.username, tweet.rawContent])
        i += 1


if __name__ == "__main__":
    asyncio.run(main())
    