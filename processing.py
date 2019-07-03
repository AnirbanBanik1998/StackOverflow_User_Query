from string import punctuation

import nltk
from nltk.stem import WordNetLemmatizer
from nltk.corpus import wordnet, stopwords
from nltk.tokenize import word_tokenize, sent_tokenize


global pos_map
pos_map = {'n': ['NN', 'NNS', 'NNP', 'NNPS'],
            'v': ['VB', 'VBD', 'VBG'],
            'a': ['JJ', 'JJR', 'JJS']}

def remove_punct(string):
    #Removes the beginning and the punctuations trailing punctuations 
    #from the words 
    new_str = ''
    tokenize = word_tokenize(string)
    for word in tokenize:
        word = word.strip(punctuation)
        if word:
            new_str += word+' '
    return new_str

def pos_tagging(string):
    #Returns the POS Tagging of the words
    tokenize = word_tokenize(string)
    tagged = nltk.pos_tag(tokenize)
    return tagged

def remove_stop_words(string):
    #Removes stop words from the string
    stop_words = set(stopwords.words('english'))
    new_str = ''
    tokenize = word_tokenize(string)
    for word in tokenize:
        if word not in stop_words:
            new_str += word+' '
    return new_str

def lemmatizer(word, tagged):
    #Returns the lemmatized output of the word
    l = WordNetLemmatizer()
    for item in tagged:
        if item[0] == word:
            for key, values in pos_map.items():
                if item[1] in values:
                    word_lemma = l.lemmatize(word, pos=key)
                    return word_lemma
    return l.lemmatize(word)


#lemmatizer = WordNetLemmatizer()
#lemmatizer.lemmatize(word, pos=None)
#syns = wordnet.synset/s(word)
#w1.wup_similarity(w2)

if __name__ == '__main__':
    inp = "How can I start to run app.js in Node.js, if I'm learning backend?"
    new_str = remove_punct(inp)
    print(new_str)
    rem_str = remove_stop_words(new_str)
    print(rem_str)
    tagged = pos_tagging(rem_str)
    print(tagged)
    arr = word_tokenize(rem_str)
    for word in arr:
        print(word + " " + lemmatizer(word, tagged))