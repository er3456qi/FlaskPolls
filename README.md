# FlaskPolls
Django tutorial project polls rewrite by Flask


database fill data(after create models):

    In[2]: from polls import db

    In[3]: from polls.models import Question, Choice

    In[4]: from datetime import datetime

    In[5]: q = Question(question_text="What's up?", pub_date=datetime.now())

    In[6]: c = Choice(choice_text="Not much", votes=0, question=q)

    In[7]: q.choice_set.append(Choice(choice_text="The sky", votes=0))

    In[8]: q.choice_set.append(Choice(choice_text="Just hacking again", votes=0))


    In[9]: db.create_all()

    In[10]: db.session.add_all([q, c])

    In[11]: db.session.commit()