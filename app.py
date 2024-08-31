from textblob import TextBlob

# Sentiment analysis scoring function
def get_sentiment_score(message):
    if message:
        # Finding score
        score = TextBlob(message).sentiment.polarity
        return score
    else:
        return 0

# Sentiment analysis labeling function
def get_sentiment_label(score):
    if score >= 0.5:
        return "Positive"
    elif score > -0.5 and score < 0.5:
        return "Neutral"
    elif score <= -0.5:
        return "Negative"
    else:
        return "N/A"

# Test data
test_messages = [
    "I love this product! It's amazing!",
    "This is the worst experience I've ever had.",
    "It's okay, not great but not bad either.",
    "",
    "The service was quite good.",
    "I absolutely loved this show",
]

# Test the functions
for message in test_messages:
    score = get_sentiment_score(message)
    label = get_sentiment_label(score)
    print(f"Message: '{message}'")
    print(f"Sentiment Score: {score}")
    print(f"Sentiment Label: {label}")
    print("-" * 40)
