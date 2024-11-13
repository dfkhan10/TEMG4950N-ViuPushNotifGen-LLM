backendState = { }

def initialize_backend_state():
    global backendState
    backendState["type_of_push_notification"] = None
    backendState["number_of_push_notifications"] = 5
    backendState["name_of_series"] = None
    backendState["retrieved_wiki_of_series"] = None
    backendState["series_content"] = None
    backendState["series_description"] = None
    backendState["name_of_cast"] = None
    backendState["type_of_cast"] = None
    backendState["nickname_of_cast"] = None
    backendState["quote_of_cast"] = None
    backendState["interesting_fact_of_cast"] = None
    backendState["character_in_series_acted_by_cast"] = None
    backendState["creativity"] = 0.2
    backendState["demographics_of_target_receiver"] = "For all ages"
    backendState["base_push_example"] = None
    backendState["local_trend_in_malaysia"] = None
    backendState["include_emoji"] = True
    backendState["include_slangs"] = True
    backendState["additional_requirements"] = None
    backendState["supporting_documents"] = None
    backendState["pushes"] = None
