def highlight_keywords(reviews):
    keywords = ["good", "excellent", "bad", "poor", "average"]
    for review in reviews:
        for word in keywords:
            review = review.replace(word, word.upper())

        print(review)




reviews = [
        "This product is really good. I'm impressed with its quality.",
        "The performance of this product is excellent. Highly recommended!",
        "I had a bad experience with this product. It didn't meet my expectations.",
        "Poor quality product. Wouldn't recommend it to anyone.",
        "The product was average. Nothing extraordinary about it."
    ]

highlight_keywords(reviews)