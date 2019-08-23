from ..extensions import db
from .abc import BaseModel, MetaBaseModel


class User(db.Model, BaseModel, metaclass=MetaBaseModel):
    """ The Task model """

    __tablename__ = "user"

    first_name = db.Column(db.String(50))
    last_name = db.Column(db.String(50))
    age = db.Column(db.Integer)
    gender = db.Column(db.String(10))


    def __init__(self, first_name, last_name, age, gender, email_id):
        """ Create a new Task """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.gender = gender
        self.email_id = emaild_id