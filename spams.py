import nltk
import pandas as pd
#nltk.download("punkt")
from nltk.tokenize import word_tokenize
from sklearn.model_selection import train_test_split

#Read external file from spam.csv
test_data_rough=pd.read_csv("spam.csv", encoding='latin-1')
test_data_trn=test_data_rough[['v1','v2']]
print(test_data_trn)

test_data,test_data_tst=train_test_split(test_data_trn, test_size=0.1)

#Load all 'spam' and 'ham' labelled texts to a list
spam_text=test_data[test_data['v1']=='spam']
ham_text=test_data[test_data['v1']=='ham']
print(spam_text)
print(ham_text)

spam_text[['v1','v2']].to_csv("spamonly.csv")
ham_text[['v1','v2']].to_csv("notspamonly.csv")
#Create new list with most popular word from spam list and ham list with stopwords removed

token_spam=[]
token_ham=[]

for i in spam_text['v2']:
    token_spam.append(word_tokenize(i))

for i in ham_text['v2']:
    token_ham.append(word_tokenize(i))

from nltk.probability import FreqDist

#print(token_spam[0:1])
#print(token_ham[0:1])

tokenspam=[]
tokenham=[]

for i in token_spam:
    for j in i:
        tokenspam.append(j)
for i in token_ham:
    for j in i:
        tokenham.append(j)

spamdist=FreqDist(tokenspam)
hamdist=FreqDist(tokenham)

#print(spamdist.most_common()[0:10])
#print(hamdist.most_common()[0:10])

#Take most popular word in spam that not popular in ham
#nltk.download('stopwords')
from nltk.corpus import stopwords
stop_words=set(stopwords.words("english"))

impspam=[]
for i in tokenspam:
    if i not in stop_words:
        impspam.append(i)

impham=[]
for i in tokenham:
    if i not in stop_words:
        impham.append(i)

spamonly=[]
for i in impspam:
    if i not in impham:
        spamonly.append(i)

spamonlydist=FreqDist(spamonly)
spamordered=spamonlydist.most_common()

#masih gajelas nih ah
spamkey=[]
for i in spamordered:
    if i[1]>4:
        spamkey.append(i[0])

print(spamkey)

#spamkey.to_csv("spamkeys.csv")

spamkeydf=pd.DataFrame(spamkey)
spamkeydf.to_csv("spamkey.csv")
test_data_tst.to_csv("spamtest.csv")


#Create counter and labeller for text with some number of spam