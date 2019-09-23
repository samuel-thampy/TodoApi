
"""
Define the REST verbs relative to the users
"""

from flasgger import swag_from
from flask.json import jsonify
from flask_restful import Resource
from flask_restful.reqparse import Argument

from ..repositories import TaskRepository
from ..util import parse_params


class TaskResource(Resource):
    """ Verbs relative to the task """

    @staticmethod
    @swag_from("../swagger/task/GET.yml")
    def get():
        """ Return an user key information based on his name """
        task = TaskRepository.get_all_by_user()
        return jsonify({"data": task})


    @staticmethod
    @parse_params(
        Argument("title", location="json", required=True, help="Create New Task")
    )
    @swag_from("../swagger/task/POST.yml")
    def post(title):
        """ Create an user based on the sent information """
        task = TaskRepository.create(title=title)
        return jsonify({"data": task.json})

