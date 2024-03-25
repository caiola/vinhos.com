import unittest
from unittest.mock import MagicMock

from api.models import Account
from api.repositories import accounts


class TestAccountRepository(unittest.TestCase):

    # TODO: Review test case
    # def test_get_by_with_id(self):
    #     # Mocking Account.query and the filter_by method to return a specific account
    #     mocked_account = Account(id=1, account_name="test_account")
    #     Account.query.filter_by = MagicMock(return_value=mocked_account)
    #
    #     result = accounts.get_by(id=1)
    #
    #     self.assertEqual(result, mocked_account)
    #     Account.query.filter_by.assert_called_once_with(id=1)

    # TODO: Review test case
    # def test_get_by_with_name(self):
    #     # Mocking Account.query and the filter_by method to return a specific account
    #     mocked_account = Account(id=1, account_name="test_account")
    #     Account.query.filter_by = MagicMock(return_value=mocked_account)
    #
    #     result = accounts.get_by(name="test_account")
    #
    #     self.assertEqual(result, mocked_account)
    #     Account.query.filter_by.assert_called_once_with(account_name="test_account")

    def test_get_by_without_parameters(self):
        with self.assertRaises(ValueError) as context:
            accounts.get_by()

        self.assertEqual(str(context.exception), "Provide id or name")

    def test_get_by_with_both_parameters(self):
        with self.assertRaises(ValueError) as context:
            accounts.get_by(id=1, name="test_account")

        self.assertEqual(str(context.exception), "Provide id or name")

    # TODO: Review test case
    # def test_get_by_no_result_found(self):
    #     # Mocking Account.query and the filter_by method to return None
    #     Account.query.filter_by = MagicMock(return_value=None)
    #
    #     with self.assertRaises(Account.DoesNotExist):
    #         accounts.get_by(id=1)
    #
    #     Account.query.filter_by.assert_called_once_with(id=1)


if __name__ == "__main__":
    unittest.main()
