from celery import Celery

app = Celery()
app.config_from_object('hellocelery.config.celery')

@app.task(bind=True)
def add(self, x, y):
    return x + y
