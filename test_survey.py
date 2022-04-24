import unittest
from survey import AnonymousSurvey

class TestAnonymousSurvey(unittest.TestCase):
    """Test classes"""

    def setUp(self):
        """setUp"""
        question = "What language did you first learn to speak?"
        self.my_survey = AnonymousSurvey(question)
        self.responses = ['English', 'Spanish', 'Mandarin']
        
    def test_store_single_response(self):
        """Check one response"""
        qeustion = "What language did you first learn to speak?"
        my_survey = AnonymousSurvey(qeustion)
        my_survey.store_response('English')

        self.assertIn('English', my_survey.responses)

    def test_store_three_repsonses(self):
        """Checks 3 results"""
        question = "What language did you first learn to speak?"
        my_survey = AnonymousSurvey(question)
        responses = ['English', 'Spanish', 'Mandarin']
        for response in responses:
            my_survey.store_response(response)

        for response in responses:
            self.assertIn(response, my_survey.responses)

unittest.main()
