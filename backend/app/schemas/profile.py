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

class ProfileCreate(BaseModel):
    """
    Pydantic model for creating a user profile.

    Attributes:
    - name: The name for the new profile.
    - description: A description or additional information for the new profile
    """
    name: str
    description: str

class ProfileUpdate(BaseModel):
    """
    Pydantic model for updating a user profile.

    Attributes:
    - name: The updated name for the profile.
    - description: The updated description for the profile.
    """
    name: str
    description: str

class ProfileInDB(ProfileCreate):
    """
    Pydantic model representing a user profile stored in the database.

    Inherits from:
    - ProfileCreate: Attributes for creating a new profile.

    Additional Attribute:
    - id: The unique identifier for the profile in the database.
    """
    id: int
