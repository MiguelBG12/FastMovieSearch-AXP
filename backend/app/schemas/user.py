from pydantic import BaseModel
from typing import List
from .profile import Profile

class UserCreate(BaseModel):
    """
    Pydantic model for creating a user.

    Attributes:
    - email: The email address for the new user.
    """
    email: str

class UserUpdate(BaseModel):
    """
    Pydantic model for updating a user.

    Attributes:
    - email: The updated email address for the user.
    - profiles: A list of profiles associated with the user.
    - favorite_profiles: A list of profiles marked as favorites by the user.
    """
    email: str
    profiles: List[Profile] = []
    favorite_profiles: List[Profile] = []

class UserInDB(UserCreate):
    """
    Pydantic model representing a user stored in the database.

    Inherits from:
    - UserCreate: Attributes for creating a new user.

    Additional Attributes:
    - id: The unique identifier for the user in the database.
    - profiles: A list of profiles associated with the user in the database.
    - favorite_profiles: A list of profiles marked as favorites by the user
    in the database.
    """
    id: int
    profiles: List[Profile] = []
    favorite_profiles: List[Profile] = []
