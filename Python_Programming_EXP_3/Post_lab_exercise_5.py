sentence = input("enter a sentence:")
words = sentence.strip().split()
longest_word = max(words, key=len)

if words:
    print(len(words[-1]))
else:
    print(len(longest_word))
