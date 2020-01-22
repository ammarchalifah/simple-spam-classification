# simple-spam-classification
Ammar
ammarchalifah.wordpress.com

This simple program classify a text message as spam/not spam. It uses NLTK and Pandas library. The mechanism behind the classification is by using a training data with spam/not spam label, and by using direct comparison between keywords from the spam and not spam categories. For words that appear in spam categories and not in not spam categories, it will be saved as spam keywords. When a test text given as an input, the program will see whether it has the spam keyword in it or not, then classify it accordingly.

This program was made for personal practice.

//HOW TO USE//
1. spam.csv is the training data used to make spam keywords. spam.csv consists of two columns, one column for label (spam/not spam), and the other one for the message.
2. spams.py extract information from spam.csv. spams.py produces three outputs: spamonly.csv (csv file consists of spam messages only from the training data), notspamonly.csv (csv file contains not-spam messages only from the training data), and spamkey.csv (all words that will be used as marker for spam messages).
3. testtext.txt is the text that we want to examine.
4. spamclass.py read spamkey.csv and testtext.txt, compare the tokenized words from testtext.txt with the keys. If there are 2 or more words that match with the spam key, then the message will be labelled as spam. If not, then otherwise.

This program uses word_tokenize and FreqDist from NLTK library.
This program uses pd.read_csv, .to_csv from Pandas.


Citations:
>Bird, Steven, Edward Loper and Ewan Klein (2009), Natural Language Processing with Python. O’Reilly Media Inc.
>Wes McKinney. Data Structures for Statistical Computing in Python, Proceedings of the 9th Python in Science Conference, 51-56 (2010) (publisher link)
