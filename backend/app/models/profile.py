from pydantic import BaseModel

class Profile(BaseModel):
    """
    Pydantic model representing a user profile.

    Attributes:
    - id: The unique identifier for the profile.
    - name: The name associated with the profile.
    - description: A description or additional information about the profile.
    """
    id: int
    name: str
    description: str

