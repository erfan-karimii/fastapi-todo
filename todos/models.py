from fastapi import Form
from pydantic import BaseModel, Field
from typing import List , Optional

class Todo(BaseModel):
    id: Optional[int] = Field(..., examples=[12])
    item: str = Field(..., examples=["read book"])
    
    @classmethod
    def as_form(
        cls,
        item: str = Form(...)
        ):
        return cls(item=item,id=0)


class TodoItem(BaseModel):
    item: str = Field(..., examples=["read book"])


class TodoItems(BaseModel):
    todos: List[TodoItem]
    
    class Config:
        schema_extra = {
        "example": {
            "todos":[
                    {
                    "item": "Example schema 1!"
                    },
                    {
                    "item": "Example schema 2!"
                    }
                ]
            }
        }