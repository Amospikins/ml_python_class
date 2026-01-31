word = input("Enter a word: ")
word_lower = word.lower()
wordToArray = list(word_lower)
wordToArray.reverse()
reversedWord = ''.join(wordToArray)
# print(reversedWord)

if word_lower == reversedWord:
    print(f"{word} is a palindrome")
else:
    print(f"{word} is not a palindrome")







