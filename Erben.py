import re
from collections import Counter


with open("polednice.txt", "r", encoding="utf-8") as f:
    text = f.read().lower()


words = re.findall(r"[a-zá-ž]+", text)
word_freq = Counter(words)

print("10 nejčastějších slov:")
for word, count in word_freq.most_common(10):
    print(word, count)


letters = [c for c in text if c.isalpha()]
letter_freq = Counter(letters)

print("\nNejčastější písmena:")
for letter, count in letter_freq.most_common(10):
    print(letter, count)


k = 3   # můžeš změnit např. na 4 nebo 5
k_words = {w for w in words if len(w) == k}

print(f"\nPočet různých {k}-písmenných slov:", len(k_words))

print(k_words)

import re
from collections import Counter


with open("polednice.txt", "r", encoding="utf-8") as soubor:
    text = soubor.read().lower()


slova = re.findall(r"[a-zá-ž]+", text)


cetnost = Counter(slova)


slovnik_jednou = {slovo: pocet for slovo, pocet in cetnost.items() if pocet == 1}


print("Slova, která se v textu vyskytují pouze jednou:")
print(slovnik_jednou)

print("Počet těchto slov:", len(slovnik_jednou))

