def reverseString(str):
    # reversed_str = str[::-1]
    revstr=''
    for char in str:

        revstr = char + revstr
    
    return revstr
    

word = input("Enter a string: ").casefold()
result = reverseString(word)
if word == result:
    print("The string is a palindrome.")
else: 
    print("The string is not a palindrome.") 

print("The reversed string is:", result)
print("hello world")