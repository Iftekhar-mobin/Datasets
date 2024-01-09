import pandas as pd
from collections import OrderedDict
import nltk
from nltk.corpus import wordnet
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
lemmatizer = WordNetLemmatizer() 

synonyms = []
antonyms = []
defi = []
exa = []
words = []
lemma = []
pos = []

txt = "drawing hobby collecting read drink peanuts interesting greeted loudest lovingly assuming excited warmly afraid glad sitting station house tightly lock picked crowed old couple corner down dried talking train watching long havy busy shopping busy place elder brother parents small town father telephone fine hello test album hit generation bed selected understand place next conversation practise above focus groups meanings recognize words sentence laughing someone noise hear name sorry meet nice imagine coming welcome student like pairs offices moment building just issuance hall library pilot lawyer patient listen language picture below nurse postman worker cleaner newspaper waiter every morning wakes walks collecting rubbish mind worker hard keep area bins put last month sick whole back realise dustbin shout present people ask question participate open day holiday table room playing ring doorbell cooking smeel good delicious favourite food usually taste sweet please elephant holding hands pairs never fail outside boxing example can look following recite individually outside some guest visit tonight think enough half about dear buy items carrots oil noodles salt sail want altogater asking garden fever burn cold problem recently sick advice flu proverb proper clinliness medicare essential regular rest physical paragraph instruction honey ancient cough ginger tea best forehead garlic pepper remedies teeth normal place clove sensitive release mane wet pain shade face debt gATe back look made hat too read add done difference between country natural resources deep plain nests lay found yellow describe chilli know simple models give paragraph beak have spot picnic activity photo text eye many glory hills rural located beauty pullers way viewers passage match gentle flow unforgettable grief memory celebrate annually independent resisting respect along promise admit defeat well sacrifice inspiration exactly feel beside suddenly reflection hairstyle flap unruly wool horns ribbons stared move quickly difficult control manage answer very bussinessman married husband died ago spend establish now nobody already often get ghost story whom miserable cues around particular boats ship river sail preety please heaven far bridge sky build road poet overtops cloud magic plane plan key say ready bike fly child drive light come carefull make government office right ride son ingredient sandwitch spread bread slice remember extra finally compare spoon pour stove break thinly serve gentle shake street blank hear improve package wrist easier try little fill numb chalk mystic bard prayer maditation recive away property publish death mankind comfort luxury crazy contain beyond eminent grow pyramid huge token took symbolise icon access remain wonder unbelievable surprise level company lesson amazing awsome fabulous construction invention sphere relative update space travel spacecraft photograph lonely impact update doubt article surprise still enjoy bundle stick oldest affectionate unite tie opposite cutting wood poor salesperson busy reply challenge peace security degree organization belong citizen clash global happen electronic entire wage earner skill economy pleasure abroad foreign job develop prefer odd else weather concert thrilled right singer song suffering during struggle war crisis distress lyrics disaster relieve passage support stand dress medium guess blue follow flat polo bit formal boring heels beach cloth print choose seem glad spring wing dreamed stout intonation hop rob rod bowl stationary hope script quiet throw blow ahead before vacation climb mountain decide suggestion fantastic expression magazine completing heavily floods rainfall vast happen period underground cause above aunt mile few plans fresh worry invitation inform whole stay miss garden frog toad seed put ground shout afraid window dark still asleep anymore planted"

wordsList = nltk.word_tokenize(txt) 

for w in wordsList:  
    for syn in wordnet.synsets(w):
        #lemma.append(lemmatizer.lemmatize(w, pos="v"))
        lemma.append(syn.lemmas()[0].name())
        words.append(w)
        #pos.append(nltk.pos_tag(w))
        pos.append(syn.pos())

        defi.append(syn.definition())
        exa.append(syn.examples())

        sy = []
        an = []
        for l in syn.lemmas():
            sy.append(l.name())
            if l.antonyms():
                an.append(l.antonyms()[0].name())
        synonyms.append(sy) 
        antonyms.append(an) 

wordDict = OrderedDict([
    ('Word', words),
    ('POS', pos),
    ('Lemma', lemma),
    ('Synonyms', synonyms),
    ('Antonyms', antonyms),
    ('Example', exa),
    ('definition', defi),
])

dict_en = pd.DataFrame.from_dict(wordDict)
dict_en["POS"] = dict_en["POS"].replace({'n': 'Noun', 'v': 'Verb', 'a':'Adjective','r':'Adverb','s':'Adjective Satellite'})
# print(dict_en.head(20))
dict_en.to_csv('dict_en.csv', encoding='utf-8')


##freq = nltk.FreqDist(wordsList) 
##for key,val in freq.items(): 
##    print (str(key) + ':' + str(val))
