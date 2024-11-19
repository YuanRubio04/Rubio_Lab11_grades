listofwords = []
matching_words = []
count = 1

while count<10:
    word = input("Enter 10 set of words: ")
    listofwords.append(word)
    count+=1
        
number=int(input("Enter a number: "))
for i in listofwords:
    if len(i)>=number:
        matching_words.append(i)
print(matching_words)
