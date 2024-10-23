from langchain_community.document_loaders import WebBaseLoader, WikipediaLoader

def webLoading(url):
    
    loader = WebBaseLoader(url)
    loaded_doc = loader.load()
    
    print("Wiki loaded according to url")
    
    return loaded_doc

def wikiLoading(query):
    
    loader = WikipediaLoader(query=query, load_max_docs=2)
    loaded_doc = loader.load()
    
    print("2 Wiki are loaded according to topic: " + query)
    
    return loaded_doc