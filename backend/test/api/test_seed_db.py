# import unittest
# from unittest.mock import patch, Mock
# from api import app, seed_db, seed_tables
#
#
# class TestSeedDB(unittest.TestCase):
#
#     # def test_seed_db_success(self):
#     #     # Mock the app.app_context() method and seed_tables function
#     #     with patch("api.app.app_context"), patch("api.seed_tables") as mock_seed_tables:
#     #         # Call the seed_db function
#     #         seed_db()
#     #
#     #         # Assert that the app.app_context() was called once
#     #         app.app_context.assert_called_once()
#     #
#     #         # Assert that the seed_tables function was called once
#     #         mock_seed_tables.assert_called_once_with(app)
#
#     # def test_seed_db_failure(self):
#     #     # Mock the app.app_context() method to raise an exception
#     #     with patch("api.app.app_context", side_effect=Exception("Something went wrong")):
#     #         # Call the seed_db function
#     #         with self.assertRaises(Exception):
#     #             seed_db()
#     #
#     #         # Assert that the app.app_context() was called once
#     #         app.app_context.assert_called_once()
#     #
#     #         # Assert that the seed_tables function was not called
#     #         self.assertFalse(seed_tables.called)
#
#
# if __name__ == "__main__":
#     unittest.main()
