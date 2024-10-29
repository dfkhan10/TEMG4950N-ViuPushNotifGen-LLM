def cast_driven_questions(series, cast):
    questions = [
        f"Retrieve the useful information of the {series}, most crucially the content and story of the character acted by {cast}. answer in long paragraphs.",
        f"What would the fans of the {cast} call him or her, are there any nicknames? answer only the name.",
        f"Does the {cast} have any famous quote? list all the quotes of the {cast} you have found, and state the origin, is it from movies or real life?",
        f"Are there any other any useful informationabout the {cast}, any fun fact or interesting incidents would be a plus, state all in paragraphs.",
        f"Who is the {cast} acting in {series}, answer in concise format."
    ]
    return questions

def content_driven_questions(series, cast = None):
    questions = [
        f"Retrieve the useful information of the {series}, most crucially the content, what is it about? answer in long paragraphs.",
    ]
    return questions