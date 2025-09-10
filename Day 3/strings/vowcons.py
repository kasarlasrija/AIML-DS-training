def vowcon(s):
    vowels = 0
    consonants = 0
    s = s.lower()
    for char in s:
        if char.isalpha():
            if char in 'aeiou':
                vowels += 1
            else:
                consonants += 1
    print("Vowels", vowels)
    print("Consonants", consonants)

str1 = "hihello"
vowcon(str1)
