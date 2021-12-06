#Exercise 2

import lightrdf

def super_topic_of(topic):
    BASE_IRI = "http://www.w3.org/2002/07/owl#"
    doc = lightrdf.RDFDocument("Lab8-1.owl")
    for triple in doc.search_triples(None, None, None):
        if "subClassOf" in triple[1] and topic in triple[2]:
            print(triple[0].split("#")[1])

#super_topic_of("ArtificialIntelligence")


#Exercise 3
import nltk
from nltk.corpus import treebank

def get_nouns_with_verb_between(from_file):
    with open(from_file) as f:
        contents = f.read()
    tokens = nltk.word_tokenize(contents)
    #print(tokens)
    tagged = nltk.pos_tag(tokens)
    #print(tagged)

    last_noun = None
    last_verb_after_noun = None 
    NOUN_TAGS = ("NN", "NNS", "NNP")
    VERB_TAGS = ("VBZ", "VBN", "BEZ", "BEG", "VBD", "VBG","VBP")


    for tag in tagged:
        if tag[1] in NOUN_TAGS:
            if last_noun == None:
                last_noun = tag[0]
            else:
                if last_verb_after_noun == None:
                    last_noun = tag[0]
                else:
                    print(f"{last_noun} : {last_verb_after_noun} : {tag[0]}")
                    last_noun = None
                    last_verb_after_noun = None
        elif tag[1] in VERB_TAGS:
            last_verb_after_noun = tag[0]


        
        
        

get_nouns_with_verb_between("computer-science.txt")


