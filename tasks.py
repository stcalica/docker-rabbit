from celery import Celery as c


app = c('tasks', broker='amqp//rabbit:5432')


@app.task
def add():
   a = 0
   b = a + 1
   return 
