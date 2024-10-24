from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import JsonOutputParser
from langchain_together import ChatTogether

llm = ChatTogether(model="meta-llama/Llama-3-70b-chat-hf", temperature=0.4)

prompt = """You are a professional digital marketer in a streaming service company Viu. Based on the following details, create a cast-driven push notification to engage the user about the latest content.

Your primary objective is to promote new TV shows to customers and provide cast-oriented information about them. And explain what information you used to generate the push.

The title consist of a appealing title.
**Sample title:** [New] The Midnight Romance in Hagwon

And consist of the body message.
**Sample message:** A former student returns to school after a decade as an instructor to be with his previous instructor 😍 Catch this Viu Original starring Wi Ha Joon & Jung Ryeo Won!

**Promoting Cast:** {target_cast}
**Cast Type:** {target_cast_type}
**Series Name:** {series_name}
**Series Description:** {series_description}
**Episode Description:** {episode_description}

The wiki document include series information and cast information, 
**Retrieved wiki document:** {wiki_description}

Do not just copy the given descriptions, promote by the cast first, and then the content of the show

Keeps the push short within 35 chars per title and 100 chars per body.
Please format the notification to be concise, engaging, and to include a call-to-action,
and output the push notification in Json format: "title", "body", "explanation". """

def generating(use_case_data, retrieved_doc):
    gen_prompt = ChatPromptTemplate.from_messages([("system", prompt)])
    chain = gen_prompt | llm | JsonOutputParser()

    document = {
        "target_cast": use_case_data["target_cast"],
        "target_cast_type": use_case_data["target_cast_type"],
        "series_name": use_case_data["series_name"],
        "series_description": use_case_data["series_description"],
        "episode_description": use_case_data["episode_description"],
        "wiki_description": retrieved_doc,
    }

    eng_push = chain.invoke(document)
    
    print(eng_push)
    
    return eng_push