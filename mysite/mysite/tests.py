from django.test import TestCase


class QuestionModelTests(TestCase):

    def test_that_should_fail(self):
        self.assertIs(True, False)

    def test_that_should_succeed(self):
        self.assertIs(True, True)
