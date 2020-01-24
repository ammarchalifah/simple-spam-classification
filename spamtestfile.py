import pandas as pd
import nltk
from nltk.tokenize import word_tokenize

spamkey=pd.read_csv("spamkey.csv", usecols=['0'])
spamlist=[]
for i in spamkey['0']:
    spamlist.append(i)

spamtest=pd.read_csv("spamtest.csv", usecols=['v2'])

#Number threshold
numb=15

#tokenize each sentence
tokentest=[]
for i in spamtest['v2']:
    tokentest.append(word_tokenize(i))

#Determining whether it is spam or not

for i in tokentest:
    count=0
    for j in i:
        count=count+1
    if count >= numb:
        print(spamtest['v2'][tokentest.index(i)]," is a spam.")
    else:
        print(spamtest['v2'][tokentest.index(i)]," is NOT a spam")
