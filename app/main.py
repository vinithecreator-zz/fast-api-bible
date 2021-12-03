from typing import List
from uuid import uuid4
from fastapi import FastAPI
from models.user import User, Gender, Role

app = FastAPI()

db: List[User] = [
    User(
        id=uuid4(),
        first_name="Marcos",
        last_name="Vinicius",
        gender=Gender.female,
        roles=[Role.user]
    ),
    User(
        id=uuid4(),
        first_name="Marvin",
        last_name="Henrique",
        gender=Gender.male,
        roles=[Role.student]
    )
]


@app.get("/")
def hello_world():
    return {"Hello": "World"}


@app.get("/api/v1/users")
async def fetch_users():
    return db;

@app.post("api/v1/users")
async def register_user(user:User):
    db.append(user)
    return {"id": user.id}
