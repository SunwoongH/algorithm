n = int(input())
word = {}

for i in range(n):
    inputWord = input()
    if inputWord not in word.keys():
        word[inputWord] = len(inputWord)

wordList = list(word.items())
wordList.sort(key = lambda x : (x[1], x[0]))

for w in wordList:
    print(w[0])