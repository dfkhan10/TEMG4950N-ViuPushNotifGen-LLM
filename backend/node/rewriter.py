from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_together import ChatTogether

llm = ChatTogether(model="meta-llama/Llama-3-70b-chat-hf", temperature=0)

def question_rewritting(state):
    prompt = PromptTemplate(
        template="""You a question re-writer that converts an input question to a better version that is optimized \n
        for vectorstore retrieval. Look at the initial and formulate an improved question. \n
        Do not change the meaning of the question. DO NOT CHAT, OUTPUT the question in ONE SENTENCE, go straight to the point.
        Here is the initial question: \n\n {question}. Improved question with no preamble: \n """,
        input_variables=["generation", "question"],
    )

    question_rewritting_chain = prompt | llm | StrOutputParser()
    
    print("---TRANSFORM QUERY---")
    
    question = state["question"]
    retry_count = state["retry_count"]


    better_question = question_rewritting_chain.invoke({"question": question})
    print(better_question)
    if retry_count >= 2:
        next = False
    else:
        next = True
        retry_count += 1
    return {"question": better_question, "retry_count": retry_count, "next": next}