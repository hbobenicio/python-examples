## Broker settings.
broker_url = 'amqp://hellocelery:hellocelery@localhost:5672//'

# List of modules to import when the Celery worker starts.
imports = ('hellocelery.app',)

## Using the database to store task state and results.
# result_backend = 'db+sqlite:///results.db'
result_backend = 'file:///tmp/celery/results/'

task_annotations = {
    'hellocelery.app.add': {
        'rate_limit': '10/s'
    }
}
