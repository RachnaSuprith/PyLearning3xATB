letters=['a','b','d','e','j','i','o','u']
def vowel_giver(letter):
    vowels=['a','e','i','o','u']
    return letter in vowels
result=vowel_giver('p')
print(result)


filtered_words=filter(vowel_giver,letters)
print(list(filtered_words))