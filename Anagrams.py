def anagrams(str1, str2):
    if sorted(str1.lower()) == sorted(str2.lower()):
        print("These words are anagrams")
    else:
        print("These words are not anagrams")


str1 = input(str("Enter a word"))
str2 = input(str("Enter a word"))
anagrams(str1, str2)
