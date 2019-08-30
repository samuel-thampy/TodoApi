import json
import unittest

from ..src.models import User
from ..src.extensions import db
from ..src.repositories import UserRepository
from ..src import app as server


class TestUser(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.client = server.test_client()

    def setUp(self):
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def test_get(self):
        """ The GET on aa`/user` should return an user """
        UserRepository.create(first_name="John", last_name="Doe", age=25,
                              gender="male", email_id="samjiks@hotmail.com")
        response = self.client.get("/api/user/Doe/John")

        self.assertEqual(response.status_code, 200)
        response_json = json.loads(response.data.decode("utf-8"))


    def test_create(self):
        """ The POST on `/user` should create an user """
        response = self.client.post(
            "/api/user/Doe/John",
            content_type="application/json",
            data=json.dumps({"age": 30, "gender": "male", "email_id": "samjiks@hotmail.com"}),
        )

        self.assertEqual(response.status_code, 200)
        response_json = json.loads(response.data.decode("utf-8"))

        self.assertEqual(User.query.count(), 1)

    def test_update(self):
        """ The PUT on `/user` should update an user's age """
        UserRepository.create(first_name="John", last_name="Doe", age=25,
                              gender="male", email_id="samjiks@hotmail.com")
        response = self.client.put(
            "/api/user/Doe/John",
            content_type="application/json",
            data=json.dumps({"age": 30}),
        )

        self.assertEqual(response.status_code, 200)
        response_json = json.loads(response.data.decode("utf-8"))

        user = UserRepository.get(first_name="John", last_name="Doe")
        self.assertEqual(user.age, 30)
