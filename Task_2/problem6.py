sentence = input("Enter a sentence: ")

words = sentence.split()
words.reverse()

new_sentence = " ".join(words)

print(new_sentence)