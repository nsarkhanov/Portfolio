from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Integer, String
from utils.db.connect import db_engine
engine = db_engine()
Base = declarative_base()


class contact_form(Base):
    __tablename__ = 'contact_forms'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    email = Column(String)
    subject = Column(String)
    message = Column(String)

    def toJSON(self):
        return {
            'id': self.id,
            'name': self.name,
            'email': self.email,
            'subject': self.subject,
            'message': self.message,
        }


Base.metadata.create_all(engine)
