from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_together import ChatTogether


llm = ChatTogether(model="meta-llama/Llama-3-70b-chat-hf", temperature=0.2)

GENERATOR_PROMPT = PromptTemplate(
    input_variables=["question", "document"],
    template="""You are an assistant for question-answering tasks about a particular show.
    Use the following pieces of retrieved context to answer the question.
    If you answer the question correctly then I will reward you with 10 dollars,
    especailly the name of the character acted by the traget actor, 
    or else I am threatening you to death.
    Use three sentences maximum and keep the answer concise."
    Here is the user question: {question}
    \n\n
    Here are the context:
    {document}
    """,
)

def testingRetrievalResult(use_case_data, retrieved_doc):
    generating_chain = GENERATOR_PROMPT | llm | StrOutputParser()

    question = "Tell me more about the character acted by " + use_case_data["target_cast"] + " in the series: " + use_case_data["series_name"]
    testing_response = generating_chain.invoke({"question": question, "document": retrieved_doc})

    print(testing_response)