
vowels = "aeiou"


vowel_count = 0
consonant_count = 0


sentence = input("Enter a sentence: ")


for char in sentence.lower():
    if char.isalpha():  
        if char in vowels:
            vowel_count += 1
        else:
            consonant_count += 1


print("Number of vowels:", vowel_count)
print("Number of consonants:", consonant_count)
