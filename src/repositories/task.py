

from ..models import Task


class TaskRepository:

    @staticmethod
    def get_all_by_user():
        """ Query a user by last and first name """
        return Task.all()


    @staticmethod
    def create(title):
        """ Create a new user """
        task = Task(title=title)

        return task.save()