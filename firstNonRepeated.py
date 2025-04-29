def firstNonRepeatedchar(str):
    count_char={}
    for char in str:
        if char in count_char:
            count_char[char] += 1
        else:
            count_char[char] = 1
    for char in str:
        if count_char[char]==1:
            return char
    return None
str='swiss'
print(firstNonRepeatedchar(str))



