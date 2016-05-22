import unittest
import datetime
from polls.models import Question

"""
The testcase is imperfect because url_for does't work
and some thing I can not handle.
"""


class QuestionMethodTests(unittest.TestCase):

    def test_was_published_recently_with_future_question(self):
        """
        was_published_recently() should return False for questions whose
        pub_date is in the future.
        """
        time = datetime.datetime.now() + datetime.timedelta(days=30)
        future_question = Question(pub_date=time)
        self.assertFalse(future_question.was_published_recently())

    def test_was_published_recently_with_old_question(self):
        """
        was_published_recently() should return False for questions whose
        pub_date is older than 1 day.
        """
        time = datetime.datetime.now() - datetime.timedelta(days=30)
        old_question = Question(pub_date=time)
        self.assertFalse(old_question.was_published_recently())

    def test_was_published_recently_with_recently_question(self):
        """
        was_published_recently() should return True for questions whose
        pub_date is within the last day.
        """
        time = datetime.datetime.now() - datetime.timedelta(hours=1)
        recent_question = Question(pub_date=time)
        self.assertTrue(recent_question.was_published_recently())


# from polls import app, db
# class PollsTestCase(unittest.TestCase):
#
#     def setUp(self):
#         import tempfile
#         app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + tempfile.mkstemp()[1]
#         app.config['TESTING'] = True
#         db.create_all()
#         self.app = app.test_client()
#
#
# def create_question(question_text, days):
#     """
#     Creates a question with the given `question_text` and published the
#     given number of `days` offset to now (negative for questions published
#     in the past, positive for questions that have yet to be published).
#     """
#     time = datetime.datetime.now() + datetime.timedelta(days=days)
#     q = Question(question_text=question_text, pub_date=time)
#     db.session.add(q)
#     db.session.commit()
#
#
# class QuestionViewTests(PollsTestCase):
#
#     def test_index_view_with_no_questions(self):
#         """
#         If no questions exist, an appropriate message should be displayed.
#         """
#         response = self.app.get(1, '/')
#         self.assertEqual(response.status_code, 200)


if __name__ == '__main__':
    unittest.main()