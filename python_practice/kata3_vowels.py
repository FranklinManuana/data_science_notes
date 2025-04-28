def numberOfVowels(data):
    vowel_count = {'a':0,'e':0,'i':0,'o':0,'u':0}
    vowels = ['a','e','i','o','u']
    for i in data:
        if i in vowels:
            vowel_count[i] = vowel_count[i] + 1
    return vowel_count
print(numberOfVowels("orange"))
print(numberOfVowels("lighthouse labs"))
print(numberOfVowels("aeiou"))
