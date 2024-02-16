def anagrams(a, b):
    a = a.replace(" ", "").upper()
    b = b.replace(" ", "").upper()

    return sorted(a) == sorted(b)


a = "Yazan"
b = "Nazay"
result = anagrams(a, b)
print(result)
