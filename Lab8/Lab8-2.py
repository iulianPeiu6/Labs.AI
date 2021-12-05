import lightrdf

doc = lightrdf.RDFDocument("Lab8-1.owl")

for triple in doc.search_triples("http://www.co-ode.org/ontologies/ont.owl#ArtificialIntelligence", None, None):
    print(triple)

lightrdf.Parser()