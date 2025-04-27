def countOccurrence(word):
    count_char = {}
    for char in word:
        if char in count_char:
            count_char[char] += 1
        else:
            count_char[char] = 1
    return count_char

word = input("Please enter your word: ")
print("Occurrences of characters are:", countOccurrence(word))