# translate
ty = input("Enter a word: ")
S = {"one": "واحد", "two": "اثنان", "three": "ثلاثه", "four": "اربعه"}
S1 = {"one": "uno", "two": "dos", "three": "tres", "four": "cuatro"}
for x in ty.split():
    try:
        result = x
        result1 = S[x]
        result2 = S1[x]
        print(result, " mean ", result1, "in Arabic language, and ", result2, "in Spanish language.")
    except:
        result3 = x
        print(result3, " is not offered in the dictionary yet.")
