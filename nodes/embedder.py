import os
import time
from pinecone import Pinecone, ServerlessSpec
from langchain_together import TogetherEmbeddings

client = Pinecone(api_key=os.getenv('PINECONE_API_KEY'))

def embedding(splits):
    
    index_name = "series-test"

    existing_indexes = [index_info["name"] for index_info in client.list_indexes()]

    if index_name not in existing_indexes:
        client.create_index(
            name=index_name,
            dimension=768,
            metric="cosine",
            spec=ServerlessSpec(cloud="aws", region="us-east-1"),
        )
        while not client.describe_index(index_name).status["ready"]:
            time.sleep(1)

    index = client.Index(index_name)

    from langchain_pinecone import PineconeVectorStore

    embeddings = TogetherEmbeddings(
        model="togethercomputer/m2-bert-80M-8k-retrieval",
        api_key=os.getenv('TOGETHER_API_KEY')
    )
    vectorstore = PineconeVectorStore(index=index, embedding=embeddings)

    vectorstore.add_documents(documents=splits)

    return vectorstore