def count(s):
    alpha= 0
    digits = 0
    specials = 0

    for i in s:
        if i.isalpha():
            alpha += 1
        elif i.isdigit():
            digits += 1
        else:
            specials += 1

    print("Alphabets:", alpha)
    print("Digits:", digits)
    print("Special characters:", specials)
text = "hihellosrija3679$"
count(text)
