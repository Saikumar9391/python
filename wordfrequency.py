from collections import Counter
import re

text = """
Python is great and Python is easy and Python is powerful.
Python helps in automation and AI.
"""

text = text.lower()

for ch in [".", ",", "!", "?", ";", ":"]:
    text = text.replace(ch, "")

words = text.split()

word_count = Counter(words)

top_5 = word_count.most_common(5)

print("Top 5 most frequent words:\n")

for word, count in top_5:
    print(f"{word} -> {count}")

text2 = """
Python is great and Python is easy and Python is powerful.
Python helps in automation and AI.
"""

words2 = re.findall(r'\b\w+\b', text2.lower())
for word in words2:
    print(word);
