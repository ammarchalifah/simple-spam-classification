import pandas as pd
import nltk
from nltk.tokenize import word_tokenize

spamkey=pd.read_csv("spamkey.csv", usecols=['0'])
#print(spamkey)

spamlist=[]
for i in spamkey['0']:
    spamlist.append(i)

#print(spamlist)

#Number of tolerance
numb=2

test=open("testtext.txt","r")
textoken=[]
for x in test:
    print(x)
    temp=word_tokenize(x)
    for b in temp:
        textoken.append(b)
    
#print(textoken)

count=0
for i in textoken:
    if i in spamlist:
        count=count+1
    if count>=numb:
        print("\n\nThis message is a spam")
        exit()

print("\n\nThis message is NOT a spam")
test.close()