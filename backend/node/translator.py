from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import JsonOutputParser
from langchain_together import ChatTogether

llm = ChatTogether(model="meta-llama/Llama-3-70b-chat-hf", temperature=0.2)

prompt = """You are a professional translator in a streaming service company Viu. Based on the following details, 

translate the given cast-driven push notification.

Your primary objective is to rewrite the english notification in Bahasa Malaye and include local slangs,
And explain how to rewrite and translate, what slang you have added.

DO NOT translate the name of the show!
DO NOT simply translate word by word, be fun!

The notification is in the following format.
**Push Notification Title:** {title}
**Push Notification Body:** {body}
**Push Notification Explanation:** {explanation}

and output ONLY the push notification in Json format:  "title", "body", "explanation". """

def engToMalay(eng_push):
    
    gen_prompt = ChatPromptTemplate.from_messages([("system", prompt)])
    malay_chain = gen_prompt | llm | JsonOutputParser()

    malay_push = malay_chain.invoke(eng_push)
    
    print(malay_push)
    
    return malay_push




# # from transformers import pipeline

# # notification_title = "[New] Uncover the Secrets with YOON Je Moon in Nothing Uncovered!"
# # notification_body = "Get ready for a thrilling ride! 🚨 YOON Je Moon stars in Nothing Uncovered, a Viu Original series about a star reporter who teams up with her ex-lover to solve a shocking incident. Don't miss out on the twists and turns! 💥 Watch now on Viu! 👉 [CTA Button: Watch Now]"

# # pipe = pipeline("text-generation", model="mesolitica/mallam-5B-4096")
# # results = pipe(notification_body)

# # print(results)

# from transformers import AutoModelForCausalLM, AutoTokenizer

# model_name = "mesolitica/mallam-5B-4096"
# question = """Translate the following: 
#     Get ready for a thrilling ride! 🚨 
#     YOON Je Moon stars in Nothing Uncovered, 
#     a Viu Original series about a star reporter who teams up with her ex-lover to solve a shocking incident. 
#     Don't miss out on the twists and turns! 💥 Watch now on Viu! 👉 [CTA Button: Watch Now]"""

# # tokenizer = AutoTokenizer.from_pretrained(model_name)
# # tokenizer.save_pretrained(f"cache1/tokenizer/{model_name}")

# # model = AutoModelForCausalLM.from_pretrained('mesolitica/mallam-5B-4096')
# # model.save_pretrained(f"cache1/model/{model_name}")

# tokenizer = AutoTokenizer.from_pretrained(f"cache1/tokenizer/{model_name}")
# model = AutoModelForCausalLM.from_pretrained(f"cache1/model/{model_name}")

# input_ids = tokenizer(question, return_tensors='pt', add_special_tokens=False)
# outputs = model.generate(**input_ids, max_new_tokens= 60)
# print(tokenizer.decode(outputs[0]))
# print(outputs)