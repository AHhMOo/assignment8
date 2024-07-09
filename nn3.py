def create_summary(review):
    if len(review) <= 30:
        return review
    
    summary = review[:30]
    
    if review[30].isalnum():
        for i in range(29, -1, -1):
            if review[i].isspace():
                summary = summary[:i]
                break
    
    summary += "…"
    
    return summary


review1 = "This product is really good. I'm very satisfied with it."
summary = create_summary(review1)
print(summary) 