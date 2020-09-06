from MyDjango.celery import app


@app.task()
def get_task():
    return 'data_clean_task'
