from collections import Counter
import string

sentences = [
 "Big data is useful and big data is growing",
 "Machine learning is used in big data",
 "Data science and machine learning are useful"
]

stopwords = {
 "the", "is", "in", "and", "a", "an", "are", "of", "to", "for", "used"
}
all_words = []

for sentence in sentences:
 sentence = sentence.lower()
 for symbol in string.punctuation:
    sentence = sentence.replace(symbol, "")
 words = sentence.split()

 filtered_words = [word for word in words if word not in stopwords]
 all_words.extend(filtered_words)

frequency = Counter(all_words)

print("Filtered word list:")
print(all_words)

print("\nTop 5 most frequent keywords:")
for word, count in frequency.most_common(5):
 print(word, ":", count)