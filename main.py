from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from db import Base, engine, get_db
from routers import authentication_router
from fastapi.staticfiles import StaticFiles
from models import Users

app = FastAPI()

Base.metadata.create_all(engine)

app.include_router(authentication_router, tags=['Authentication'])

@app.get('/')
def get_users(db: Session = Depends(get_db)):
    return db.quert(Users).all()