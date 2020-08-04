def is_isogram(string):
    words = string.lower().replace('-', '').split()
    for word in words:
        for char in word:
            if word.count(char) > 1:
                return False
    return True
