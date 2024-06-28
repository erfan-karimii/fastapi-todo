from fastapi import FastAPI
from todo import todo_router

app = FastAPI()
app.include_router(todo_router)

@app.post("/",status_code=200)
def welcome() -> dict:
    return { "message": "Hello World"}