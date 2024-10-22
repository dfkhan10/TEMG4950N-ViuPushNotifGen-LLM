from src.data import getCastDrivenData
from nodes import loader, splitter, embedder, retriever, generator, translator

def castDrivenPipeline(cast, datasets):
    
    print("___Start Handling Data___")
    cast_driven_data = getCastDrivenData(cast, datasets)
    
    print("___Start Loading___")
    series_wiki = loader.webLoading(cast_driven_data["series_wiki_url"])
    
    print("___Start Splitting___")
    splitted_series_wiki = splitter.splitting(series_wiki)
    
    print("___Start Embedding___")
    series_vectorstore = embedder.embedding(splitted_series_wiki)
    
    print("___Start Retrieval___")
    cast_retrieved_info = retriever.retrieving(series_vectorstore, cast)
    
    print("___Start Generation___")
    eng_push = generator.generating(cast_driven_data, cast_retrieved_info)
    
    print("___Start Translation___")
    malay_push = translator.engToMalay(eng_push)
    
    print(eng_push)
    print(malay_push)