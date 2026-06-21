sentence = input("Enter a sentence: ")

longestword = ""

for word in sentence.split():
    if len(word) > len(longestword):
        longestword = word

print(f"Longest word: {longestword}")
