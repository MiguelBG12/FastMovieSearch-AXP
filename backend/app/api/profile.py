from fastapi import APIRouter, HTTPException
from typing import List
from ..models.profile import Profile
from ..schemas.profile import ProfileCreate, ProfileUpdate, ProfileInDB

router = APIRouter()

# List of example profiles to simulate the database
fake_profiles_db: List[ProfileInDB] = []

@router.post("/profiles/", response_model=Profile)
def create_profile(profile: ProfileCreate):
    """
    Create a new profile.

    Parameters:
    - profile (ProfileCreate): The data for creating a new profile.

    Returns:
    - Profile: The created profile.
    """
    # Check if the profile already exists by name
    existing_profile = next((p for p in fake_profiles_db if p.name == profile.name), None)
    if existing_profile:
        raise HTTPException(status_code=400, detail="Profile already exists")
    
    new_profile = Profile(id=len(fake_profiles_db) + 1, **profile.dict())
    fake_profiles_db.append(new_profile)
    return new_profile

@router.get("/profiles/{profile_id}", response_model=Profile)
def read_profile(profile_id: int):
    """
    Get a profile by its ID.

    Parameters:
    - profile_id (int): The ID of the profile.

    Returns:
    - Profile: The requested profile.
    """
    profile = next((p for p in fake_profiles_db if p.id == profile_id), None)
    if profile is None:
        raise HTTPException(status_code=404, detail="Profile not found")
    return profile

@router.put("/profiles/{profile_id}", response_model=Profile)
def update_profile(profile_id: int, profile: ProfileUpdate):
    """
    Update a profile by its ID.

    Parameters:
    - profile_id (int): The ID of the profile to update.
    - profile (ProfileUpdate): The data for updating the profile.

    Returns:
    - Profile: The updated profile.
    """
    existing_profile = next((p for p in fake_profiles_db if p.id == profile_id), None)
    if existing_profile is None:
        raise HTTPException(status_code=404, detail="Profile not found")

    # Update profile fields
    for field, value in profile.dict(exclude_unset=True).items():
        setattr(existing_profile, field, value)

    return existing_profile

@router.delete("/profiles/{profile_id}", response_model=Profile)
def delete_profile(profile_id: int):
    """
    Delete a profile by its ID.

    Parameters:
    - profile_id (int): The ID of the profile to delete.

    Returns:
    - Profile: The deleted profile.
    """
    profile = next((p for p in fake_profiles_db if p.id == profile_id), None)
    if profile is None:
        raise HTTPException(status_code=404, detail="Profile not found")
    fake_profiles_db.remove(profile)
    return profile

@router.get("/profiles/", response_model=List[ProfileInDB])
def get_profiles():
    """
    Get a list of all profiles.

    Returns:
    - List[ProfileInDB]: A list of profiles.
    """
    return fake_profiles_db
