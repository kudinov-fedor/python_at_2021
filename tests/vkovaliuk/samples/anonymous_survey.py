class AnonymousSurvey:
    def __init__(self, question):
        self.question = question
        self.responses = []

    def show_question(self):
        print(self.question)

    def append_response(self, new_response):
        self.responses.append(new_response)

    def remove_response(self, response_to_remove):
        self.responses.remove(response_to_remove)

    def sort_survey_responses(self, reverse=False):
        return self.responses.sort(reverse=reverse)

    def show_all_responses(self):
        for response in self.responses:
            print(f"- {response}")
