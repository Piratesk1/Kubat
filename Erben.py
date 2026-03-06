import re
from collections import Counter

# načtení souboru
with open("polednice.txt", "r", encoding="utf-8") as f:
    text = f.read().lower()

# -------------------------
# 1. frekvence slov
# -------------------------
words = re.findall(r"[a-zá-ž]+", text)
word_freq = Counter(words)

print("10 nejčastějších slov:")
for word, count in word_freq.most_common(10):
    print(word, count)

# -------------------------
# 2. frekvence písmen
# -------------------------
letters = [c for c in text if c.isalpha()]
letter_freq = Counter(letters)

print("\nNejčastější písmena:")
for letter, count in letter_freq.most_common(10):
    print(letter, count)

# -------------------------
# 3. počet různých k-písmenných slov
# -------------------------
k = 3   # můžeš změnit např. na 4 nebo 5
k_words = {w for w in words if len(w) == k}

print(f"\nPočet různých {k}-písmenných slov:", len(k_words))

print(k_words)

import re
from collections import Counter

# načtení textu ze souboru
with open("polednice.txt", "r", encoding="utf-8") as soubor:
    text = soubor.read().lower()

# rozdělení textu na jednotlivá slova
slova = re.findall(r"[a-zá-ž]+", text)

# spočítání četnosti slov
cetnost = Counter(slova)

# vytvoření slovníku slov, která se v textu vyskytují pouze jednou
slovnik_jednou = {slovo: pocet for slovo, pocet in cetnost.items() if pocet == 1}

# výpis výsledku
print("Slova, která se v textu vyskytují pouze jednou:")
print(slovnik_jednou)

print("Počet těchto slov:", len(slovnik_jednou))
