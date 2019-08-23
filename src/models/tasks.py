

from .extensions import db
from abc import BaseModel, MetaBaseModel


class Task(db.Model, BaseModel, metaclass=MetaBaseModel):
    """ The Task model """

    __tablename__ = "task"

    title = db.Column(db.String(500))

    def __init__(self, title):
        """ Create a new Task """
        self.title = title


class TaskUser(db.Model, BaseModel, metaclass=MetaBaseModel):
    """ The Task model """

    __tablename__ = "task_user"

    task_id = db.Column(Integer, ForeignKey('task.id'))
    user_id = db.Column(Integer, ForeignKey('user.id'))


class TaskSchedule(db.Model, BaseModel, metaclass=MetaBaseModel):
    """ The Task Schedule model """

    __tablename__ = "task_schedule"

    scheduled_time = db.Column(db.DateTime)
    task_id = db.Column(Integer, ForeignKey('task.id'))


    def __init__(self, scheduled_time):
        """ Create a new Task """
        self.scheduled_time = scheduled_time

