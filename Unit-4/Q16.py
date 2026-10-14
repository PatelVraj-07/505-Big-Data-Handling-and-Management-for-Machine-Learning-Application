from transformers import pipeline

summarizer = pipeline(
    "text-generation",
    model="Qwen/Qwen2.5-0.5B-Instruct"
)

article = """
Big data refers to very large and complex datasets that traditional
data-processing methods may not handle efficiently. Organizations use
big data technologies to store, process, and analyze information from
many sources. Apache Spark supports distributed data processing and
can perform tasks such as filtering, aggregation, and machine learning.
Machine learning models can use prepared data to make predictions.
Text-processing models can also classify sentiment and summarize long
documents to help readers understand important information quickly.
"""

prompt = f"""Summarize the following article in simple English
using a few sentences.

Article:
{article}

Summary:
"""

result = summarizer(
    prompt,
    max_new_tokens=100,
    do_sample=False,
    return_full_text=False
)

print("Original article:")
print(article)

print("\nGenerated summary:")
print(result[0]["generated_text"].strip())