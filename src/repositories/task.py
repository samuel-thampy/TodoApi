

from ..models import Task


class TaskRepository:

    @staticmethod
    def create(title):
        """ Create a new user """
        task = Task(title=title)

        return task.save()