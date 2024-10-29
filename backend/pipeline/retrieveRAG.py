from typing import List
from langchain_pinecone import PineconeVectorStore
from typing_extensions import TypedDict
from langgraph.graph import END, StateGraph, START
from node import retriever, grader, generator, rewriter

class GraphState(TypedDict):
    vectorstore: PineconeVectorStore
    question: str
    generation: str = None
    documents: List[str] = []
    retry_count: int = 0
    next: bool = True

workflow = StateGraph(GraphState)

def pass_grading(state):
    return state["next"]

def fail_answering(state):
    return {"generation": None}

workflow.add_node("retrieve", retriever.retrieving) 
workflow.add_node("grade_documents", grader.retrieval_grading)  
workflow.add_node("grade_hallcination", grader.hallucination_grading)
workflow.add_node("grade_answer", grader.answer_grading)
workflow.add_node("generate", generator.generating)  
workflow.add_node("rewrite_question", rewriter.question_rewritting)
workflow.add_node("fail_answering", fail_answering)

workflow.add_edge(START, "retrieve")
workflow.add_edge("retrieve", "grade_documents")
workflow.add_conditional_edges(
    "grade_documents",
    pass_grading,
    {
        True: "generate",
        False: "rewrite_question",
    },
)
workflow.add_conditional_edges(
    "generate",
    pass_grading,
    {
        True: "grade_hallcination",
        False: "fail_answering",
    },
)
workflow.add_conditional_edges(
    "grade_hallcination",
    pass_grading,
    {
        True: "grade_answer",
        False: "generate",
    },
)
workflow.add_conditional_edges(
    "grade_answer",
    pass_grading,
    {
        True: END,
        False: "rewrite_question",
    },
)
workflow.add_conditional_edges(
    "rewrite_question",
    pass_grading,
    {
        True: "retrieve",
        False: "fail_answering",
    },
)
workflow.add_edge("fail_answering", END)

retrieval_RAG_pipeline = workflow.compile()