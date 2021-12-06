#Exercise 2
import lightrdf

def super_topic_of(topic):
    doc = lightrdf.RDFDocument("Lab8-1.owl")
    for triple in doc.search_triples(None, None, None):
        if "subClassOf" in triple[1] and topic in triple[2]:
            print(triple[0].split("#")[1])

#super_topic_of("ArtificialIntelligence")


#Exercise 3
import nltk

def get_nouns_with_verb_between(from_file):
    with open(from_file) as f:
        contents = f.read()
    
    sentences = nltk.tokenize.sent_tokenize(contents)

    NOUN_TAGS = ("NN", "NNS", "NNP")
    VERB_TAGS = ("VBZ", "VBN", "BEZ", "BEG", "VBD", "VBG","VBP")
    fout = open("result_3.txt", 'w')
    
    for sentence in sentences:
        tokens = nltk.word_tokenize(sentence)
        tagged = nltk.pos_tag(tokens)

        last_noun = None
        last_verb_after_noun = None 
        
        for tag in tagged:
            if tag[1] in NOUN_TAGS:
                if last_noun == None:
                    last_noun = tag[0]
                else:
                    if last_verb_after_noun == None:
                        last_noun = tag[0]
                    else:
                        fout.write(f"{sentence}\r\n")
                        break
            elif tag[1] in VERB_TAGS:
                last_verb_after_noun = tag[0]

    f.close()
        
        
get_nouns_with_verb_between("computer-science.txt")

#Exercise 4

def filter_file_content(file):
    BASE_IRI = "http://www.co-ode.org/ontologies/ont.owl#"
    doc = lightrdf.RDFDocument("Lab8-1.owl")
    file_content = open("result_3.txt", 'r')
    fwrite = open("result_4.txt", 'w')
    for line in file_content:
        current_line = line.rstrip()
        found = False
        keywords = nltk.word_tokenize(current_line)
        for keyword in keywords:
            for triple in doc.search_triples(f"{BASE_IRI}{keyword.lower()}", None, None):
                found = True
                break
            if found:
                print(line)
                fwrite.write(line)
                break
            

filter_file_content("result_4.txt")