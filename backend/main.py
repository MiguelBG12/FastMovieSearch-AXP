from fastapi import FastAPI
from app.api import user, profile
from fastapi.openapi.docs import get_redoc_html, get_swagger_ui_html
from fastapi.middleware.cors import CORSMiddleware

# Configuration of allowed origins for CORS
origins = [
    "http://localhost:5173",
]

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include the routes from API modules
app.include_router(user.router, prefix="/users", tags=["users"])
app.include_router(profile.router, prefix="/profiles", tags=["profiles"])

# Configuration to expose documentation at the root path
app.get("/docs", include_in_schema=False)(get_swagger_ui_html)
app.get("/redoc", include_in_schema=False)(get_redoc_html)
