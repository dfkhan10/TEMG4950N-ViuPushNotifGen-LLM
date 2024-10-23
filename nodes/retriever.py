def retrieving(vectorstore, cast, series_name):

    retriever = vectorstore.as_retriever(search_kwargs={"k": 6})
    question = "Tell me more about the character acted by " + cast + " in the series: " + series_name
    retrieved_doc = retriever.invoke(question)
    
    print("The following are retrieved:")
    for doc in retrieved_doc:
        print(doc)
    
    return retrieved_doc

# Retriever for series wiki -> Poor efficiency, prompt requires modification
# WIKIPEDIA is not enough, not much can be retrieved without web crawling more stuff