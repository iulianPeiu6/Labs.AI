import lightrdf

def superTopicOf(topic):
    BASE_IRI = "http://www.w3.org/2002/07/owl#"
    doc = lightrdf.RDFDocument("Lab8-1.owl")
    for triple in doc.search_triples(None, None, None):
        if "subClassOf" in triple[1] and topic in triple[2]:
            print(triple[0].split("#")[1])
            
superTopicOf("ArtificialIntelligence")