"""
Defines the blueprint for the users
"""
from flask import Blueprint
from flask_restful import Api

from ..resources import TaskResource

TASK_BLUEPRINT = Blueprint("task", __name__)

Api(TASK_BLUEPRINT).add_resource(
    TaskResource, "/task"
)
