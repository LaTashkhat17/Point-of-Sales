from fastapi import FastAPI
from app.database import engine, Base
from app import models
from app.routes import users

app = FastAPI(title="SaaS AI POS System")

# Create tables in the database
models.Base.metadata.create_all(bind=engine)

# Include the users router
app.include_router(users.router, prefix="/users", tags=["Users"])

@app.get("/")
async def root():
    return {"message": "POS system!"}
