
# change the index if u saw ? * \\

# if we have \ in the text we can find it with that method 
#a = "adksajfkdajfk\a"
#"\\" in r"%r" % a

def contains(text, pattern):
    for i in range(len(text)):
        for j in range(len(pattern)):
            #Out of range
            if i + j >= len(text):
                break
            #If does not match with pattern
            print(text[i])
            if pattern[j] == "*" or pattern[j] == "\\" or pattern[j] == "?":
                j +=1
                if j == len(pattern):
                    return True       
            if text[i + j] != pattern[j] and (pattern[j] != "\\" or pattern[j] != "*" or pattern[j] != "?"):
                break
        else:
            return True
    return False

text = "ab\tdabadccdbabd"
pattern = '?da'
print(text)
print(contains(text,pattern))

#you can controll the ?,* and \ character from ascii table

