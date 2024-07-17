from assets.file import all_biomes as RAW
result = []
def extract_chars_after_word(text, word, num_chars=50):
    index = 0
    while True:
        # Sucht das Wort im Text ab der aktuellen Position
        index = text.find(word, index)
        if index == -1:
            break
        
        # Berechnet den Startindex des Substrings
        start_index = index + len(word)
        
        # Berechnet den Endindex des Substrings
        end_index = start_index + num_chars
        
        # Extrahiert den Substring
        substring = text[start_index:end_index]
        
        # Gibt den Substring aus
        if substring not in result:
            result.append(substring)
        
        # Setzt den Startindex für die nächste Suche
        index = end_index

# Beispieltext und Wort
text = (
    "Das ist ein Beispieltext. Das Wort, nach dem gesucht wird, ist 'Beispieltext'. "
    "Danach folgen weitere interessante Informationen. Dies ist ein weiterer Beispieltext, "
    "um zu demonstrieren, wie das Programm funktioniert. Hier steht noch mehr Text, der das "
    "Wort Beispieltext enthält und weitere 100 Zeichen extrahiert werden sollen."
)
word = "biome"

# Funktion aufrufen
extract_chars_after_word(RAW, word)
print(result)