from sqlalchemy.orm import Session
from app.domain.models.tag import Tag

def get_all_tags(db: Session):
    return db.query(Tag).all()

def create_tag(db: Session, tag: Tag):
    db.add(tag)
    db.commit()
    db.refresh(tag)
    return tag
