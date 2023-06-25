guess_word=input()
ned_perm=input()
c1=0
c2=len(guess_word)
word=["_"]*c2
filled=set()
for letter in ned_perm:
    if c1==10:
        break
    else:
        if letter in guess_word and letter not in filled:
            filled.add(letter)
            for j in range(c2):
                if guess_word[j]==letter:
                    word[j]=letter
        else:
            c1+=1

win=True
for k in range(c2):
    if word[k]==guess_word[k]:
        continue
    else:
        win=False
if win:
    print("WIN")
else:
    print("LOSE")
