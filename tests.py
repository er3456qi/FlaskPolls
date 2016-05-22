import unittest
import tempfile
import datetime
from polls import app, db
from polls.models import Question


class PollsTestCase(unittest.TestCase):

    def setUp(self):
        app.config['SQLALCHEMY_DATABASE_URI'] = tempfile.mktemp()
        self.app = app.test_client()


class QuestionMethodTests(PollsTestCase):

    def test_was_published_recently_with_future_question(self):
        """
        was_published_recently() should return False for questions whose
        pub_date is in the future.
        """
        time = datetime.datetime.now() + datetime.timedelta(days=30)
        future_question = Question(pub_date=time)
        self.assertFalse(future_question.was_published_recently())


if __name__ == '__main__':
    unittest.main()