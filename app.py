from flask import Flask
from celery import Celery

app = Flask(__name__)
app.config['CELERY_BROKER_URL'] = 'redis://localhost:6379/0'
app.config['CELERY_RESULT_BACKEND'] = 'redis://localhost:6379/0'

<<<<<<< HEAD
celery = Celery(app.name, broker=app.config['CELERY_BROKER_URL'])
celery.conf.update(app.config)
=======
result = q.enqueue(count_words_at_url, 'http://heroku.com')
print(result)
>>>>>>> e5ac0772f2188b7f024c4b2a81b24fba68417aa3
