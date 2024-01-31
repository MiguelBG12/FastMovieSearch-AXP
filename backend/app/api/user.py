from fastapi import APIRouter, HTTPException
from typing import List
from ..models.user import User
from ..schemas.user import UserCreate, UserUpdate, UserInDB

router = APIRouter()

# List of example users to simulate the database
fake_users_db: List[UserInDB] = []

@router.post("/", response_model=User, summary="Create a new user")
def create_user(user: UserCreate):
    """
    Create a new user.

    Parameters:
    - user (UserCreate): The data for creating a new user.

    Returns:
    - User: The created user.
    """
    # Check if the user already exists by email
    existing_user = next((u for u in fake_users_db if u.email == user.email), None)
    if existing_user:
        raise HTTPException(status_code=400, detail="User already exists")
    
    new_user = User(id=len(fake_users_db) + 1, email=user.email)
    fake_users_db.append(new_user)
    return new_user

@router.get("/{user_id}", response_model=UserInDB, summary="Get user by ID")
def read_user(user_id: int):
    """
    Get a user by its ID.

    Parameters:
    - user_id (int): The ID of the user.

    Returns:
    - UserInDB: The requested user.
    """
    user = next((u for u in fake_users_db if u.id == user_id), None)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return user

@router.put("/{user_id}", response_model=UserInDB, summary="Update one user")
def update_user(user_id: int, user: UserUpdate):
    """
    Update a user by its ID.

    Parameters:
    - user_id (int): The ID of the user to update.
    - user (UserUpdate): The data for updating the user.

    Returns:
    - UserInDB: The updated user.
    """
    existing_user = next((u for u in fake_users_db if u.id == user_id), None)
    if existing_user is None:
        raise HTTPException(status_code=404, detail="User not found")

    # Update user fields
    existing_user.email = user.email
    existing_user.profiles = user.profiles
    existing_user.favorite_profiles = user.favorite_profiles

    return existing_user

@router.delete("/{user_id}", response_model=UserInDB, summary="Delete one user")
def delete_user(user_id: int):
    """
    Delete a user by its ID.

    Parameters:
    - user_id (int): The ID of the user to delete.

    Returns:
    - UserInDB: The deleted user.
    """
    user = next((u for u in fake_users_db if u.id == user_id), None)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    fake_users_db.remove(user)
    return user

@router.get("/", response_model=List[UserInDB], summary="Retrieve all the users")
def get_users():
    """
    Get a list of all users.

    Returns:
    - List[UserInDB]: A list of users.
    """
    return fake_users_db
