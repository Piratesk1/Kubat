# ---------------------------------------------
# VELKÝ PROGRAM PRACUJÍCÍ S LISTEM (SEZNAMEM)
# ---------------------------------------------

# 1) Vytvoření listu ze zkopírovaného seznamu
print("1) Vytvářím počáteční seznam...")
seznam = ["ChatGPT", "Claude", "Gemini", "Llama"]
print("Původní seznam:", seznam)
print("-" * 50)

# 2) Přidání nové položky
print("2) Přidávám novou položku 'Mistral'...")
seznam.append("Mistral")
print("Seznam po přidání:", seznam)
print("-" * 50)

# 3) Odstranění prvního prvku
print("3) Odstraňuji první prvek seznamu...")
prvni = seznam.pop(0)
print(f"Odstraněn prvek: {prvni}")
print("Seznam po odstranění:", seznam)
print("-" * 50)

# 4) Vypsání délky seznamu
print("4) Délka seznamu:", len(seznam))
print("-" * 50)

# 5) Vypsání celého seznamu
print("5) Výsledný seznam:")
for index, prvek in enumerate(seznam, start=1):
    print(f"{index}. {prvek}")

print("-" * 50)
print("Program dokončen.")
