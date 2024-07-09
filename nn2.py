def count_positive_negative_words(review):
    # Define lists of positive and negative words
    positive_words = ["good", "excellent", "great", "awesome", "fantastic", "superb", "amazing"]
    negative_words = ["bad", "poor", "terrible", "horrible", "awful", "disappointing", "subpar"]
    
    # Convert review to lowercase and split into words
    words = review.lower().split()
    
    # Initialize counters for positive and negative words
    positive_count = 0
    negative_count = 0
    
    # Count positive words
    for word in words:
        if word in positive_words:
            positive_count += 1
    
    # Count negative words
    for word in words:
        if word in negative_words:
            negative_count += 1
    
    # Return the counts
    return positive_count, negative_count
review1 = "This movie is good and excellent, but the acting is terrible."
pos_count, neg_count = count_positive_negative_words(review1)
print(f"Positive words count: {pos_count}")
print(f"Negative words count: {neg_count}")
