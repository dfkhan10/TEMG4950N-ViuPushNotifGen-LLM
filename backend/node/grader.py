from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser
from langchain_together import ChatTogether

llm = ChatTogether(model="meta-llama/Llama-3-70b-chat-hf", temperature=0)


def retrieval_grading(state):
    prompt = PromptTemplate(
        input_variables=["question", "document"],
        template="""You are a grader assessing relevance of a retrieved document to a user question. 
        If the document contains keywords related to the user question, grade it as relevant. 
        It does not need to be a stringent test. The goal is to filter out erroneous retrievals.
        Give a binary score 'yes' or 'no' score to indicate whether the document is relevant to the question.
        Provide the binary score as a JSON with a single key 'score' and no premable or explanation.
        Here is the retrieved document: {document}
        Here is the user question: {question}
        """,
    )

    retrieval_grading_chain = prompt | llm | JsonOutputParser()
    
    print("---CHECK DOCUMENT RELEVANCE TO QUESTION---")
    
    question = state["question"]
    documents = state["documents"]

    filtered_docs = []
    for d in documents:
        score = retrieval_grading_chain.invoke(
            {"question": question, "document": d.page_content}
        )
        grade = score["score"]

        if grade.lower() == "yes":
            print("---GRADE: DOCUMENT RELEVANT---")
            filtered_docs.append(d)

        else:
            print("---GRADE: DOCUMENT NOT RELEVANT---")
            continue
        
    if not filtered_docs:
        print("---DECISION: ALL DOCUMENTS ARE NOT RELEVANT TO QUESTION---")
        next = False
    else:
        print("---DECISION: GENERATE---")
        next = True

    return {"documents": filtered_docs, "next": next}


def hallucination_grading(state):
    prompt = PromptTemplate(
        template="""You are a grader assessing whether an answer is grounded in / supported by a set of facts. 
        Give a binary 'yes' or 'no' score to indicate whether the answer is grounded in / supported by a set of facts. 
        Provide the binary score as a JSON with a single key 'score' and no preamble or explanation.
        Here are the facts:
        \n ------- \n
        {documents}
        \n ------- \n
        Here is the answer: {generation}""",
        input_variables=["generation", "documents"],
    )

    hallucination_grading_chain = prompt | llm | JsonOutputParser()
    
    print("---CHECK HALLUCINATIONS---")
    
    generation = state["generation"]
    documents = state["documents"]
    retry_count = state["retry_count"]

    score = hallucination_grading_chain.invoke({"documents": documents, "generation": generation})
    grade = score["score"]

    if grade == "yes":
        print("---DECISION: GENERATION IS GROUNDED IN DOCUMENTS---")
        return {"next": True}
    else:
        print("---DECISION: GENERATION IS NOT GROUNDED IN DOCUMENTS, RE-TRY---")
        return {"next": False, "retry_count": retry_count + 1}


def answer_grading(state):
    prompt = PromptTemplate(
        template="""You are a grader assessing whether an answer is useful to resolve a question. 
        Give a binary score 'yes' or 'no' to indicate whether the answer is useful to resolve a question. 
        Provide the binary score as a JSON with a single key 'score' and no preamble or explanation.
        Here is the answer:
        \n ------- \n
        {generation}
        \n ------- \n
        Here is the question: {question}""",
        input_variables=["generation", "question"],
    )

    answer_grading_chain = prompt | llm | JsonOutputParser()

    print("---GRADE GENERATION vs QUESTION---")
    
    generation = state["generation"]
    question = state["question"]
    
    score = answer_grading_chain.invoke({"question": question, "generation": generation})
    grade = score["score"]
    
    if grade == "yes":
        print("---DECISION: GENERATION ADDRESSES QUESTION---")
        return {"generation": generation, "next": True}
    else:
        print("---DECISION: GENERATION DOES NOT ADDRESS QUESTION---")
        return {"next": False}
