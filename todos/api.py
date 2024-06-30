from fastapi import FastAPI
from todo import todo_router
from render import todo_render_router


app = FastAPI()
app.include_router(todo_router)
app.include_router(todo_render_router)



@app.post("/", status_code=200)
def welcome() -> dict:
    return {"message": "Hello World"}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run("api:app", reload=True)


# uvicorn api:app --reload
