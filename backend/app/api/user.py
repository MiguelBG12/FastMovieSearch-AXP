from fastapi import APIRouter, HTTPException
from typing import List
from ..models.user import User
from ..schemas.user import UserCreate, UserUpdate, UserInDB

router = APIRouter()

# Lista de usuarios de ejemplo para simular la base de datos
fake_users_db: List[UserInDB] = []

@router.post("/users/", response_model=User)
def create_user(user: UserCreate):
    # Verificar si el usuario ya existe por su correo electrónico
    existing_user = next((u for u in fake_users_db if u.email == user.email), None)
    if existing_user:
        raise HTTPException(status_code=400, detail="User already exists")
    
    new_user = User(id=len(fake_users_db) + 1, email=user.email)
    fake_users_db.append(new_user)
    return new_user

@router.get("/users/{user_id}", response_model=UserInDB)
def read_user(user_id: int):
    user = next((u for u in fake_users_db if u.id == user_id), None)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return user

@router.put("/users/{user_id}", response_model=UserInDB)
def update_user(user_id: int, user: UserUpdate):
    existing_user = next((u for u in fake_users_db if u.id == user_id), None)
    if existing_user is None:
        raise HTTPException(status_code=404, detail="User not found")

    # Actualizar campos del usuario
    existing_user.email = user.email
    existing_user.profiles = user.profiles
    existing_user.favorite_profiles = user.favorite_profiles

    return existing_user

@router.delete("/users/{user_id}", response_model=UserInDB)
def delete_user(user_id: int):
    user = next((u for u in fake_users_db if u.id == user_id), None)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    fake_users_db.remove(user)
    return user

@router.get("/users/", response_model=List[UserInDB])
def get_users():
    return fake_users_db
