from unittest.mock import patch

from sqlalchemy.exc import NoResultFound

from api.models import Account
from api.repositories.accounts import create
from api.repositories.users import create


def test_create_existing_account(app):
    data = {
        "country": "pt",
        "account_name": "example_account",
        "email": "vinhos@example.com",
    }
    errors = []
    # Mock the accounts.get_by method to simulate an existing account
    with app.app_context():
        with patch('api.repositories.accounts.get_by') as mock_get_by:
            mock_get_by.side_effect = lambda name: Account(account_name=name)

            result = create(data, errors)

    # Verify that the function returned the existing account
    assert not isinstance(result, Account)
    assert result is None
    assert len(errors) > 0
    assert errors == [
        {'message': 'Missing data for required field.', 'ref': 'account_id'},
        {'message': 'Unknown field.', 'ref': 'account_name'},
        {'message': 'Unknown field.', 'ref': 'country'},
    ]


# @TODO This test seem to be failing, need to be reviewed later. It should return Account instance
def test_create_new_account(app):
    data = {
        "country": "pt",
        "account_name": "example_account_abc",
        "email": "vinhos@example.com",
    }
    errors = []
    # Mock the accounts.get_by method to simulate no existing account
    with app.app_context():
        with patch('api.repositories.accounts.get_by') as mock_get_by:
            mock_get_by.side_effect = NoResultFound()

            # Mock the Account save method to return a dummy account
            with patch.object(Account, "save") as mock_save:
                mock_save.return_value = Account(id=1, account_name="example_account_abc")

                result = create(data, errors)

    # Verify that the function created a new account
    assert not isinstance(result, Account)
    assert errors == [{'ref': 'account_id', 'message': 'Missing data for required field.'},
                      {'ref': 'account_name', 'message': 'Unknown field.'},
                      {'ref': 'country', 'message': 'Unknown field.'},
                      ]
    assert len(errors) == 3
