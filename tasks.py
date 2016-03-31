from celery import Celery as c


app = c('tasks', backend="amqp", broker='localhost')

@app.task 
def hello():
 print 'hello there'
