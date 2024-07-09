def count_positive_negative_words(review):
    positive_words = ["good", "excellent", "great", "awesome", "fantastic", "superb", "amazing"]
    negative_words = ["bad", "poor", "terrible", "horrible", "awful", "disappointing", "subpar"]
    
    words = review.lower().split()
    
    positive_count = 0
    negative_count = 0
    
    for word in words:
        if word in positive_words:
            positive_count += 1
    
    for word in words:
        if word in negative_words:
            negative_count += 1
    
    return positive_count, negative_count
review1 = "This movie is good and excellent, but the acting is terrible."
pos_count, neg_count = count_positive_negative_words(review1)
print(f"Positive words count: {pos_count}")
print(f"Negative words count: {neg_count}")
