class AnonymousSurvey():
    """Survey"""

    def __init__(self, question):
        self.question = question
        self.responses = []

    def show_question(self):
        """Выводит вопрос."""

        print(question)

    def store_response(self, new_response):
        """Save"""
        self.responses.append(new_response)

    def show_results(self):
        """Out all res"""
        print("Survey results:")
        for response in responses:
            print('- ' + response)