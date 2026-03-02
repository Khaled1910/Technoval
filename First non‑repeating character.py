def non_repeated_char(string):
    freq = {}
    # for i in string:
    #     if i not in freq:
    #         freq[i] = 1
    #     else:
    #         freq[i] += 1
    for i in string:
        freq[i] = freq.get(i,0) + 1
    for j in string:
        if freq[j] == 1:
            print(j)
            break

word = list(input("enter a word: "))
non_repeated_char(word)
