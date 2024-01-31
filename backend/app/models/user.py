from pydantic import BaseModel
from typing import List
from .profile import Profile

class User(BaseModel):
    """
    Pydantic model representing a user.

    Attributes:
    - id: The unique identifier for the user.
    - email: The email address associated with the user.
    - profiles: A list of profiles associated with the user.
    - favorite_profiles: A list of profiles marked as favorites by the user.
    """
    id: int
    email: str
    profiles: List[Profile] = []
    favorite_profiles: List[Profile] = []
