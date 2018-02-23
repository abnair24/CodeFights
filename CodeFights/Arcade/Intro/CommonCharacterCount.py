def commonCharacterCount(s1, s2):
    count = 0
    for i in range(0, len(s1)):
        for j in range(0, len(s2)):
            if s1[i] == s2[j]:
                count = count + 1
                s2 = s2[:j] + s2[(j+1):]
                break
    return count


print("Enter string s1: ")
s1 = input()
print("Enter string s2: ")
s2 = input()
print(commonCharacterCount(s1, s2))



