from celery import Celery
from app.math_utils import add, subtract

celery = Celery("tasks", broker="redis://redis:6379/0")

@celery.task
def add_task(a: int, b: int) -> int:
    return add(a, b)

@celery.task
def subtract_task(a: int, b: int) -> int:
    return subtract(a, b)
