from langchain_community.document_loaders import WebBaseLoader

def webLoading(url):
    
    loader = WebBaseLoader(url)
    loaded_doc = loader.load()
    
    return loaded_doc