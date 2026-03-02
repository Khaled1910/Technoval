first_word=input("Enter the first word:  ")
second_word=input("Enter the second word:  ")
first_word="".join(sorted(first_word.replace(" ","").lower()))
second_word="".join(sorted(second_word.replace(" ","").lower()))
if first_word == second_word:
    print("Anagrams")
else:
    print("Not Anagrams")    