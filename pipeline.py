from src.data import getCastDrivenData
from node import loader, splitter, embedder, retriever, generator, translator, tester
from model.push_notification import PushResponse

def castDrivenPipeline(cast, push_number, datasets = "Viu_datasets"):
    
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
    eng_pushes = generator.generating(cast_driven_data, cast_retrieved_info, push_number)
    
    print("___Start Translation___")
    pushes = {}
    for idx, eng_push in enumerate(eng_pushes):
        pushes[idx + 1] = PushResponse(eng_push=eng_push, malay_push=translator.engToMalay(eng_push))
    
    print("___End of Pipeline___")    
    return pushes