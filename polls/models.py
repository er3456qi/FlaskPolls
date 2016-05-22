import datetime
from polls import db


class Question(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    question_text = db.Column(db.String(200))
    pub_date = db.Column(db.DateTime)
    choice_set = db.relationship('Choice', backref='question')

    def was_published_recently(self):
        return self.pub_date >= datetime.datetime.now() - datetime.timedelta(days=1)

    def __str__(self):
        return self.question_text


class Choice(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    choice_text = db.Column(db.String(200))
    question_id = db.Column(db.Integer, db.ForeignKey('question.id'))
    votes = db.Column(db.Integer)

    def __str__(self):
        return self.choice_text