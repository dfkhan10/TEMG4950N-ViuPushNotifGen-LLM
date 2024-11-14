from dotenv import load_dotenv
load_dotenv(override=True)

from utils import slang
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_together import ChatTogether

llm = ChatTogether(model="meta-llama/Llama-3-70b-chat-hf", temperature=0.4)

def prepare_context(slang_data, shortform_data):
    slang_context = "\n".join(
        [f"{entry['word']}: {entry['meaning']} ({entry['explaination']}) Example: {entry['example']}" for entry in slang_data]
    )

    shortform_context = "\n".join(
        [f"{entry['short-form word']}: {entry['normal word']} ({entry['meaning']})" for entry in shortform_data]
    )

    return slang_context, shortform_context

def rephrase(push):
    slangs, shortforms = prepare_context(slang.slang_list, slang.shortform_list)

    prompt = PromptTemplate(
        input_variables=["pushes", "slangs", "shortforms"],
        template = """You are an assistant that enhances text by incorporating local slang and short forms.
        Below is a set of push notifications in JSON format and a list of slang or shortform. Your task is to enhance only the Malay versions of 
        the notifications by adding appropriate slang and short forms while keeping the English versions and the 
        overall JSON structure intact. 
        
        Never overshoot the slang and short forms, only add them if they are appropriate.

        Never change the emojis or the hashtags in the push notifications.

        You must always return valid JSON formatted with double quotes and without any additional text.
        Here is the push notifications in JSON: {pushes}
        \n\n
        Here are some slang: {slangs}
        Here are some shortform: {shortforms}

        Use escape characters for quotes if there is in the JSON strings.
        The output format have to be JSON as follows! The number is the push number:
        {{
        "1": {{"english": {{"title": "title", "body": "body"}}, "malay": {{"title": "title", "body": "body"}}}},
        "2": {{"english": {{"title": "title", "body": "body"}}, "malay": {{"title": "title", "body": "body"}}}},
        "3": {{"english": {{"title": "title", "body": "body"}}, "malay": {{"title": "title", "body": "body"}}}},
        ...
        }}
        Return only valid JSON without any additional text or explanations infront or after.
        Do not include anything else other than the JSON, or the output will be invalid.
        """
    )

    chain = prompt | llm | StrOutputParser()

    return chain.invoke({"pushes": push,  "slangs": slangs, "shortforms": shortforms})