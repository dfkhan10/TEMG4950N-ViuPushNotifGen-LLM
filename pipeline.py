from src.data import getCastDrivenData
from node import loader, splitter, embedder, retriever, generator, translator, tester

def castDrivenPipeline(cast, datasets = "Viu_datasets"):
    
    print("___Start Handling Data___")
    cast_driven_data = getCastDrivenData(cast, datasets)
    
    print("___Start Loading___")
    series_wiki = loader.webLoading(cast_driven_data["series_wiki_url"])
    cast_wiki = loader.wikiLoading(cast)
    
    print("___Start Splitting___")
    splitted_wiki = splitter.splitting([series_wiki, cast_wiki])
    
    print("___Start Embedding___")
    series_vectorstore = embedder.embedding(splitted_wiki, cast)
    
    print("___Start Retrieval___")
    cast_retrieved_info = retriever.retrieving(series_vectorstore, cast, cast_driven_data["series_name"])
    tester.testingRetrievalResult(cast_driven_data, cast_retrieved_info)
    
    print("___Start Generation___")
    eng_push = generator.generating(cast_driven_data, cast_retrieved_info)
    
    print("___Start Translation___")
    malay_push = translator.engToMalay(eng_push)
    
    return eng_push, malay_push