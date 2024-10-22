def retrieving(vectorstore, cast):

    retriever = vectorstore.as_retriever(search_kwargs={"k": 6})
    question = "Who is acted by " + cast
    retrieved_doc = retriever.invoke(question)
    
    return retrieved_doc

# Retriever for series wiki -> Poor efficiency, prompt requires modification
# WIKIPEDIA is not enough, not much can be retrieved without web crawling more stuff