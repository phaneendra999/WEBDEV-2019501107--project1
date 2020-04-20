import requests
res = requests.get("https://www.goodreads.com/book/review_counts.json", params={"key": "f9gk7B7jYajYHt0YM4Yuw", "isbns": "9781632168146"})
print(res.json())