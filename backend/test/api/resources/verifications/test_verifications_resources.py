import unittest
from datetime import datetime
from unittest.mock import patch

from flask_restful import reqparse

from api.models import Verification
from api.resources.verifications import VerificationsUserResource


# Helper function to create a fake verification result for testing
def create_fake_verification_result(id_val=1, date_created="2023-07-02 12:00:00"):
    date_format = "%Y-%m-%d %H:%M:%S"
    return Verification(
        **{"id": id_val, "date_created": datetime.strptime(date_created, date_format)}
    )


class TestVerificationsUserResource(unittest.TestCase):
    def setUp(self):
        self.resource = VerificationsUserResource()
        self.parser = reqparse.RequestParser()
        self.parser.add_argument(
            "page",
            type=int,
            default=1,
            help="Current page",
            required=False,
            location="args",
        )
        self.parser.add_argument(
            "size",
            type=int,
            default=20,
            help="Number of records per page",
            required=False,
            location="args",
        )

    @patch("api.repositories.verifications.verify")
    def test_get_successful_verification(self, mock_verify):
        # Mock the verifications.verify function to return a fake verification result
        fake_user_id = 123
        fake_token = "fake_token"
        data = {
            "user_id": fake_user_id,
            "token": fake_token,
            "type": "user",
        }
        mock_verify.return_value = create_fake_verification_result()

        # Make a GET request to the resource
        response, http_status_code = self.resource.get(fake_user_id, fake_token)

        # Assertions
        self.assertEqual(http_status_code, 200)
        self.assertIn("id", response)
        self.assertEqual(response["id"], 1)
        self.assertIn("date_created_utc", response)

    @patch("api.repositories.verifications.verify")
    def test_get_verification_with_errors(self, mock_verify):
        # Mock the verifications.verify function to return errors
        fake_user_id = 456
        fake_token = "invalid_token"
        data = {
            "user_id": fake_user_id,
            "token": fake_token,
            "type": "user",
        }
        fake_errors = ["Invalid token provided.", 201]
        mock_verify.return_value = None
        mock_verify.return_value = fake_errors

        # Make a GET request to the resource
        response, http_status_code = self.resource.get(fake_user_id, fake_token)

        # Assertions
        self.assertEqual(http_status_code, 400)
        # @TODO: Refine the following tests
        # self.assertIn("errors", response)
        # self.assertEqual(response["errors"], fake_errors)


if __name__ == "__main__":
    unittest.main()
