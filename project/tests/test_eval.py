import json

from project.tests.base import BaseTestCase


class TestEvalBlueprint(BaseTestCase):

    def test_ping(self):
        """Ensure the /ping route behaves correctly."""
        response = self.client.get("/ping", headers={"Authorization": "Bearer test"})
        data = json.loads(response.data.decode())
        self.assert200(response)
        self.assertIn("pong!", data["message"])
        self.assertIn("success", data["status"])

    def test_ping_no_header(self):
        """Ensure error is thrown in 'Authorization' header is empty."""
        response = self.client.get("/ping")
        data = json.loads(response.data.decode())
        self.assert403(response)
        self.assertIn("Provide a valid auth token.", data["message"])
        self.assertIn("error", data["status"])
