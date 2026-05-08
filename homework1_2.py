# h.w1: create a simple app, then push it to local then cloud repostiory
# h.w2: create a simple app , to count the number of characters ,word , sentences

character=input("enter character: ")
word=input("enter word : ")
sentece=input("enter sentece :")
c=len(character)
w=len(word)
s=len(sentece.replace(" ",""))
print(f" the number of character is {c} , the number of character in word is {w} ,the number of character in sentect is {s} ")