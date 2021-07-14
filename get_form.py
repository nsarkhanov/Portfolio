from utils.db.connect import db_engine
from utils.db.models.user import contact_form
from sqlalchemy.orm import Session
# db instance
engine = db_engine()
# session instance
session = Session(engine, future=True)


def create_form(name, email, subject, message):
    user = contact_form(name=name, email=email,
                        subject=subject, message=message)
    session.add(user)
    session.commit()
    return user.toJSON()


def get_users():
    result = [row.toJSON() for row in session.query(create_form)]
    return result


def get_users_by_id(id):
    user = session.query(create_form).get(id)
    if(user):
        return user.toJSON()
    return None


def update_user_by_id(id, update):
    user = session.query(create_form).get(id)
    if(user):
        for key, value in update.items():
            setattr(user, key, value)
        session.commit()
        return user.toJSON()
    return None


def delete_user_by_id(id):
    user = session.query(create_form).get(id)
    if(user):
        session.delete(user)
        session.commit()
        return user.toJSON()
    return None
