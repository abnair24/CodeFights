# //Given an encoded string, return its corresponding decoded string.
# //
# //        The encoding rule is: k[encoded_string], where the encoded_string inside the
# // square brackets is repeated exactly k times. Note: k is guaranteed to be a positive integer.
# //
# //        Note that your solution should have linear complexity because this is what you will be asked during an interview.
# //
# //        Example
# //
# //        For s = "4[ab]", the output should be
# //        decodeString(s) = "abababab";
# //
# //        For s = "2[b3[a]]", the output should be
# //        decodeString(s) = "baaabaaa";
# //
# //        For s = "z1[y]zzz2[abc]", the output should be
# //        decodeString(s) = "zyzzzabcabc".


def reverse_parentheses(s):
    num = ""
    start = 0
    x = 0
    for i in range(len(s)):
        if s[i].isdigit():
            num = num + s[i]
            x = num
        if s[i] == "[":
            num = ""
            start = i
        if s[i] == "]":
            end = i
            return reverse_parentheses(s[:start-(len(x)-1)-1] + s[start+1:end] * int(x) + s[end+1:])
    return s


print(reverse_parentheses("10[code2[fights]]"))