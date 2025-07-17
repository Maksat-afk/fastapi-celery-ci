from fastapi import FastAPI
from app.tasks import add_task

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Welcome!"}

@app.get("/add")
def add(a: int, b: int):
    task = add_task.delay(a, b)
    return {"task_id": task.id}
