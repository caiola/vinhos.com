import unittest

from werkzeug.security import check_password_hash

from api.models import User


class TestUserModel(unittest.TestCase):
    def setUp(self):
        # Create a test user
        self.test_user = User(email="test@example.com")

    def test_set_password(self):
        # Test setting the password for the user
        password = "secure_password"
        self.test_user.set_password(password)

        # Ensure the password_hash is not empty
        self.assertIsNotNone(self.test_user.password_hash)

        # Ensure the password_hash is a string
        self.assertIsInstance(self.test_user.password_hash, str)

        # Ensure the password_hash is not equal to the password (hashed)
        self.assertNotEqual(self.test_user.password_hash, password)

    def test_check_password(self):
        # Test checking the password for the user
        password = "secure_password"
        self.test_user.set_password(password)

        # Check with correct password
        self.assertTrue(self.test_user.check_password(password))

        # Check with incorrect password
        self.assertFalse(self.test_user.check_password("incorrect_password"))


if __name__ == "__main__":
    unittest.main()
