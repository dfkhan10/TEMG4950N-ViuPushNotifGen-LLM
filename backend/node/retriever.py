from typing import List
from langchain_together import ChatTogether
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import BaseOutputParser
from langchain.retrievers.multi_query import MultiQueryRetriever

llm = ChatTogether(model="meta-llama/Llama-3-70b-chat-hf", temperature=0)

class LineListOutputParser(BaseOutputParser[List[str]]):
    """Output parser for a list of lines."""
    def parse(self, text: str) -> List[str]:
        lines = text.strip().split("\n")
        return list(filter(None, lines))

def retrieving(state):

    QUERY_PROMPT = PromptTemplate(
        input_variables=["question"],
        template="""You are an AI language model assistant. Your task is to generate five
        different versions of the given user question to retrieve relevant documents from a vector
        database. By generating multiple perspectives on the user question, your goal is to help
        the user overcome some of the limitations of the distance-based similarity search.
        Provide these alternative questions separated by newlines.
        Original question: {question}""",
    )

    retrieving_chain = QUERY_PROMPT | llm | LineListOutputParser()

    print("---RETRIEVE---")
    question = state["question"]
    vectorstore = state["vectorstore"]

    retriever = MultiQueryRetriever(
        retriever = vectorstore.as_retriever(search_type="mmr"),
        llm_chain = retrieving_chain,
        parser_key = "lines"
    )

    documents = retriever.invoke(question)

    return {"documents": documents, "question": question}

def wiki_retrieving(vectorstore, cast, series_name):

    retriever = vectorstore.as_retriever(search_kwargs={"k": 6})
    question = "Tell me more about the character acted by " + cast + " in the series: " + series_name
    retrieved_doc = retriever.invoke(question)
    
    print("The following are retrieved:")
    for doc in retrieved_doc:
        print(doc)
    
    return 
    
def wiki_content_retrieving(vectorstore, series_name):

    retriever = vectorstore.as_retriever(search_kwargs={"k": 6})
    question = "Tell me more about the series: " + series_name
    retrieved_doc = retriever.invoke(question)
    
    print("The following are retrieved:")
    for doc in retrieved_doc:
        print(doc)
    
    return