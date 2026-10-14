from transformers import pipeline

sentiment = pipeline("sentiment-analysis")

reviews = [
 "The product is excellent and I am very happy.",
 "The service was terrible and very slow.",
 "The quality is good and delivery was quick."
]

results = sentiment(reviews)
    
for review, result in zip(reviews, results):
 print("Review:", review)
 print("Sentiment:", result["label"])
 print("Confidence score:", round(result["score"], 4))
 print()