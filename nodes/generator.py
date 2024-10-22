from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_together import ChatTogether

llm = ChatTogether(model="meta-llama/Llama-3-70b-chat-hf", temperature=0.2)

prompt = """You are a professional digital marketer in a streaming service company Viu. Based on the following details, create a cast-driven push notification to engage the user about the latest content.

Your primary objective is to promote new TV shows to customers and provide information about them.

The title consist of a appealing title.
**Sample title:** [New] The Midnight Romance in Hagwon

And consist of the body message.
**Sample message:** A former student returns to school after a decade as an instructor to be with his previous instructor 😍 Catch this Viu Original starring Wi Ha Joon & Jung Ryeo Won!

**Promoting Cast:** {target_cast}
**Cast Type:** {target_cast_type}
**Series Name:** {series_name}
**Series Description:** {series_description}
**Episode Description:** {episode_description}

**Retrieved wiki document:** {wiki_description}

Please format the notification to be concise, engaging, and to include a call-to-action."""

def generating(use_case_data, retrieved_doc):
    gen_prompt = ChatPromptTemplate.from_messages([("system", prompt)])
    chain = gen_prompt | llm | StrOutputParser()

    document = {
        "target_cast": use_case_data["target_cast"],
        "target_cast_type": use_case_data["target_cast_type"],
        "series_name": use_case_data["series_name"],
        "series_description": use_case_data["series_description"],
        "episode_description": use_case_data["episode_description"],
        "wiki_description": retrieved_doc,
    }

    eng_push = chain.invoke(document)
    
    return eng_push