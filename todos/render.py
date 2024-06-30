from fastapi import APIRouter,HTTPException,status ,Request,Depends,Path
from fastapi.templating import Jinja2Templates

from models import Todo, TodoItem, TodoItems



todo_list = []
todo_render_router = APIRouter(prefix='')
templates = Jinja2Templates(directory="templates/")


@todo_render_router.post("/todo")
async def add_todo(request: Request, todo: Todo = Depends(Todo.as_form)):
    todo.id = len(todo_list) + 1
    todo_list.append(todo)
    return templates.TemplateResponse("todo.html",{
    "request": request,
    "todos": todo_list
    })

@todo_render_router.get("/todo", response_model=TodoItems)
async def retrieve_todo(request: Request):
    return templates.TemplateResponse("todo.html", {
    "request": request,
    "todos": todo_list
    })

@todo_render_router.get("/todo/{todo_id}")
async def get_single_todo(request: Request, todo_id: int = Path(..., title="The ID of the todo to retrieve.")):
    for todo in todo_list:
        if todo.id == todo_id:
            return templates.TemplateResponse(
            "todo.html", {
            "request": request,
            "todo": todo
            })
    raise HTTPException(
    status_code=status.HTTP_404_NOT_FOUND,)