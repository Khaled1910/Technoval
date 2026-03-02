sentence = input("Enter a sentence: ")
words = sentence.split()
hashmap = {}
for i in words:
    if i in hashmap:
        hashmap[i] += 1
    else:
        hashmap[i] = 1
print(hashmap)
