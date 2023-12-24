from typing import Union

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class User(BaseModel):
    id: int
    name: str
    age: int
    email: str
    password: str

users_list = [User(id = 1, name = "Gabriel", age = 20, email = "gabriellopezromero@gmail.com", password= "lolo1311"), User(id=2, name="Bernabella", age="20", email="bernamarchetti@gmail.com", password="bernita0409")]


@app.get("/users")
async def users():
    return "Hola Users!"

@app.get("/users/{user_id}")
async def get_user(user_id: int):
    return search_user_id(user_id)

def search_user_id(id: int):
    try:
        users = filter(lambda user: user.id == id, users_list)
        return list(users)[0]
    except:
        return "El usuario no existe."
