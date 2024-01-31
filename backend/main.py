from fastapi import FastAPI
from app.api import user, profile
from fastapi.openapi.docs import get_redoc_html, get_swagger_ui_html

app = FastAPI()


# Include the routes from API modules
app.include_router(user.router, prefix="/users", tags=["users"])
app.include_router(profile.router, prefix="/profiles", tags=["profiles"])

# Configuration to expose documentation at the root path
app.get("/docs", include_in_schema=False)(get_swagger_ui_html)
app.get("/redoc", include_in_schema=False)(get_redoc_html)
