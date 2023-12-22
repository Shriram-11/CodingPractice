def isanagram(s1, s2):
    if sorted(s1) == sorted(s2):
        print("Anagrams")
    else:
        print("Not Anagrams")
