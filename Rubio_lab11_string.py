count = 0
listofwords = []
matching_words = []

for i in range(10):
        while True:
            word = input("Enter a word: ")
        listofwords.append(word)
        count+=1

number=int(input("Enter a number: "))
for i in listofwords:
    if len(i)>=number:
        matching_words.append(i)
print(matching_words)
        
    
