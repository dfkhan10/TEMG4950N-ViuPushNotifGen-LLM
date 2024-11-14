from langchain_core.prompts import PromptTemplate, FewShotPromptTemplate
from utils.example import examples

example_prompt = PromptTemplate.from_template(
    """
    Given:
    type_of_push_notification={type_of_push_notification},
    number_of_push_notifications={number_of_push_notifications},
    name_of_series={name_of_series},
    series_content={series_content},
    series_description={series_description},
    name_of_cast={name_of_cast},
    type_of_cast={type_of_cast},
    nickname_of_cast={nickname_of_cast},
    quote_of_cast={quote_of_cast},
    interesting_fact_of_cast={interesting_fact_of_cast},
    character_in_series_acted_by_cast={character_in_series_acted_by_cast},
    demographics_of_target_receiver={demographics_of_target_receiver},
    base_push_example={base_push_example},
    local_trend_in_malaysia={local_trend_in_malaysia},
    include_emoji={include_emoji},
    include_slangs={include_slangs},
    additional_requirements={additional_requirements},
    
    The following juicy push notification for {name_of_series} is generated as below:
    english_title={english_title},
    english_body={english_body},
    malay_title={malay_title},
    malay_body={malay_body}
    """
)

final_prompt = FewShotPromptTemplate(
    examples = examples,
    example_prompt = example_prompt,
    suffix = """
    Generate {number_of_push_notifications} {type_of_push_notification} push notifications for the Viu TV show "{name_of_series}".
    Exaggerate and be a clickbait in the push!
    
    Each push notification should be generated in both English and Bahasa Melayu.
    Exaggerate and be a clickbait in the push!
    
    The push notifications need to be very juicy and tempting to attract users to click.
    Exaggerate and be a clickbait in the push!
    
    Use a hook at the front, which can be the cast, content, trend, news, cast quote, series content, or memes—anything you think would be attractive.
    Exaggerate and be a clickbait in the push!
    
    Be creative and make the push notification as juicy as you can, and it can be longer.
    Exaggerate and be a clickbait in the push!
    
    Write the most important and attractive content in the first 100 characters of the body, ensuring the cast name and series name appear within these characters.
    Exaggerate and be a clickbait in the push!
    
    Each push notification must contain a title and a body. 
    Exaggerate and be a clickbait in the push!
    
    Add a call to action. Include hashtags at the end.
    Exaggerate and be a clickbait in the push!
    
    Be very juicy and not boring, and be creative.
    Exaggerate and be a clickbait in the push!
    
    The push must contain the more content of the show, it is fine to have the push being long.
    Exaggerate and be a clickbait in the push!
    
    If there are any extra requirements by the user, you must fulfill them while keeping the push interesting.
    All input data may be None; use those that are not None and choose which ones to use by yourself.
    Aim to generate the best clickbait {type_of_push_notification} notification.
    
    If "Type of Push Notification" is cast-driven, "name_of_cast" must be included in the push.
    If "Demographics of the target receiver of the push", please adjust the push according to the target receiver demographics, which is 
        be more energetic for younger receivers,
        be more cast-focus and use more information of the cast when the target receivers are fan on the cast
    If "Base Push Example" is provided, improve and regenerate a push based on the "Base Push Example".
    If "Local trend in Malaysia" is provided, the trend must be incoporated into the push with any method.
    If "Include Slangs" is True, please incorporate local slangs in the Bahasa Melayu version.
    If and only if "Include Emoji" is True, please se emojis.
    
    The followings are additional requirements that must be fulfiled when generating the push notification.
    {additional_requirements}

    The following information will be input into the prompt, choose wisely which to incoporate in the push, use more as you can:
    - Number of push notifications: {number_of_push_notifications}
    - Name of the series: {name_of_series}
    - Retrieved wiki of the series: {retrieved_wiki_of_series}
    - Series content: {series_content}
    - Series description: {series_description}
    - Name of the cast: {name_of_cast}
    - Type of cast={type_of_cast},
    - Nickname of the cast: {nickname_of_cast}
    - Quote of the cast: {quote_of_cast}
    - Interesting fact of the cast: {interesting_fact_of_cast}
    - Character in the series acted by the cast: {character_in_series_acted_by_cast}
    
    - Demographics of the target receiver of the push: {demographics_of_target_receiver}

    - Base Push Example: {base_push_example}
    - Local trend in Malaysia: {local_trend_in_malaysia}
    - Include Emoji: {include_emoji}
    - Include Slangs: {include_slangs}
    - Additional requirements from the user: {additional_requirements}

    TThe output format have to be JSON as follows! The number is the push number:
    {{
    "1": {{"english": {{"title": "title", "body": "body"}}, "malay": {{"title": "title", "body": "body"}}}},
    "2": {{"english": {{"title": "title", "body": "body"}}, "malay": {{"title": "title", "body": "body"}}}},
    "3": {{"english": {{"title": "title", "body": "body"}}, "malay": {{"title": "title", "body": "body"}}}},
    ...
    }}
    Never include anything else other than the JSON, 
    Never include descriptions or commments in the output, infront JSON or after JSON, 
    else the output will be invalid.""",
    
    input_variables=[
        "type_of_push_notification",
        "number_of_push_notifications",
        "name_of_series",
        "retrieved_wiki_of_series",
        "series_content",
        "series_description",
        "name_of_cast",
        "nickname_of_cast",
        "quote_of_cast",
        "interesting_fact_of_cast",
        "character_in_series_acted_by_cast",
        "demographics_of_target_receiver",
        "base_push_example",
        "local_trend_in_malaysia",
        "include_emoji",
        "include_slangs",
        "additional_requirements",
    ],
)