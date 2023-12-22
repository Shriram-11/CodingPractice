def showfrequency(c, s):
    if c in s:
        print(f"{c}\t{s.count(c)}")
    else:
        print("Character not in string")
