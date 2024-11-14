from langchain_community.document_loaders import WebBaseLoader, WikipediaLoader

def webLoading(url):
    
    loaded_doc = None
    try:
        loader = WebBaseLoader(url)
        loaded_doc = loader.load()
        print("Wiki loaded according to url")
    except:
        print("Error loading Wiki according to url")
    
    return loaded_doc

def wikiLoading(query):
    
    loaded_doc = None
    try:
        loader = WikipediaLoader(query=query, load_max_docs=2)
        loaded_doc = loader.load()
        print("2 Wiki are loaded according to topic: " + query)
    except:
        print("Error loading Wiki according to topic: " + query)
    
    return loaded_doc