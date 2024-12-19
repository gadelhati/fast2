from fastapi import Body, FastAPI, HTTPException
from api.config import engine
from sqlalchemy.exc import SQLAlchemyError

from api.models import model
from api.router import router

try:
    model.Base.metadata.create_all(bind=engine)
except SQLAlchemyError as e:
    raise RuntimeError(f"Error creating tables in the database: {e}")

app = FastAPI()

@app.get("/")
async def home():
    return {"message": "Welcome Home", "status": "success"}

app.include_router(router, prefix="/book", tags=["book"])