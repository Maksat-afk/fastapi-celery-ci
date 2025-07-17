from celery_worker import celery

@celery.task
def add_task(a: int, b: int):
    return a + b
