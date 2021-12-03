from typing import List
from uuid import uuid4
from fastapi import FastAPI
from models.user import User, Gender, Role

application = FastAPI()

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


@application.get("/api/v1/health")
async def health_check():
    message = {'message': 'Application its healthy}'}
    return message if (db is True) else {'message': 'Database is offline'}


@application.get("/")
async def hello_world():
    return {"message": "Hello World"}


@application.get("/api/v1/users")
async def fetch_users():
    return db;


@application.post("api/v1/users")
async def register_user(user: User):
    db.append(user)
    return {"id": user.id}
