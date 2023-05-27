import sqlalchemy 

from models import Users
from sqlalchemy.orm import Session, joinedload
from sqlalchemy import func, or_, and_

def create_crud(req, model, db: Session):
    new_add = model(**req.dict())
    db.add(new_add)
    db.commit()
    db.refresh(new_add)
    return new_add 



def signUp(req, db: Session):
    print(req)
    user = db.query(Users).filter(
        and_(
            Users.username == req.username,
            Users.password == req.password
        )
    ).first()
    if user: 
        return False
    new_add = Users(**req.dict())
    db.add(new_add)
    db.commit()
    db.refresh(new_add)
    return True


def signIn(req, db: Session):
    user = db.query(Users).filter(
        and_(
            Users.username == req.username,
            Users.password == req.password
        )
    ).first()
    if user:
        return True
    
def read_users(db: Session):
    return db.query(Users.id, Users.email, Users.username).all()
