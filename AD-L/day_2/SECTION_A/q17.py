character_inp = input("Enter a character: ")

if character_inp.lower() in "aeiou":
    print(f"{character_inp} is a vowel.")
else:
    print(f"{character_inp} is a consonant.")
