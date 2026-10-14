import string

text = " Hello!!! Big DATA, is useful... for ML applications. "

clean_text = text.lower()

for symbol in string.punctuation:
 clean_text = clean_text.replace(symbol, "")

clean_text = " ".join(clean_text.split()).strip()

tokens = clean_text.split()

print("Original text:")
print(text)

print("\nCleaned text:")
print(clean_text)

print("\nWord tokens:")
print(tokens)