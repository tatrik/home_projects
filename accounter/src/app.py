from fastapi import FastAPI

from src.api import router


tags_metadata = [
    {
        'name': 'auth',
        'description': 'Logging in and registering'
    },
    {
        'name': 'operations',
        'description': 'CRUD of operations'
    },
    {
        'name': 'reports',
        'description': 'Import and export of reports'
    },
]


app = FastAPI(
    title="Accountant",
    description="service for income and expense accounting",
    version='1.0.0'
)
app.include_router(router)
