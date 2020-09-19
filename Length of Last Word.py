def lengthOfLastWord(s):
    words = s.strip().split(' ')
    return len(words[-1])

print(lengthOfLastWord("hello world "))