def count(s):
    v="aeiouAEIOU"
    vowel=0
    consonant=0
    for char in s:
        if char.isalpha():
            if char in v:
                vowel+=1
            else:
                consonant+=1
    print(f"{vowel},{consonant}")
s=input()
count(s)
