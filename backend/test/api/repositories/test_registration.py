from unittest.mock import patch

from sqlalchemy.exc import NoResultFound

from api.models import Account
from api.repositories import accounts
from api.repositories.accounts import create


def test_create_existing_account(app):
    data = {
        "country": "pt",
        "account_name": "example_account",
        "email": "vinhos@example.com",
    }
    errors = []
    # Mock the accounts.get_by method to simulate an existing account
    with app.app_context():
        with patch.object(accounts, "get_by") as mock_get_by:
            mock_get_by.return_value = Account(account_name="example_account")

            result = create(data, errors)

    # Verify that the function returned the existing account
    assert isinstance(result, Account)
    assert result is not None
    assert len(errors) > 0
    assert errors == [{"ref": "account", "message": "Account name already exists"}]


def test_create_new_account(app):
    data = {
        "country": "pt",
        "account_name": "example_account_abc",
        "email": "vinhos@example.com",
    }
    errors = []
    # Mock the accounts.get_by method to simulate no existing account
    with app.app_context():
        with patch("api.repositories.accounts.get_by") as mock_get_by:
            with patch("pycountry.countries.get") as mock_countries_by:
                mock_get_by.side_effect = NoResultFound()

                # It is wrong but should fallback to "pt" anyways
                mock_countries_by.side_effect = "pt"

                # Mock the Account save method to return a dummy account
                with patch.object(Account, "save") as mock_save:
                    mock_save.return_value = Account(
                        id=123, account_name="example_account"
                    )

                    result = create(data, errors)

    # Verify that the function created a new account
    assert isinstance(result, Account)
    assert errors == []
    assert len(errors) == 0


def test_create_new_account_with_empty_data(app):
    data = {}
    errors = []
    # Mock the accounts.get_by method to simulate no existing account
    with app.app_context():
        with patch("api.repositories.accounts.get_by") as mock_get_by:
            mock_get_by.side_effect = NoResultFound()

            # Mock the Account save method to return a dummy account
            with patch.object(Account, "save") as mock_save:
                mock_save.return_value = None

                result = create(data, errors)

    # Verify that the function created a new account
    assert not isinstance(result, Account)
    assert errors == [
        {"ref": "account", "message": "Data is empty."},
    ]
    assert len(errors) == 1


def test_create_new_account_with_empty_fields(app):
    data = {
        "country": "",
        "account_name": "",
        "email": "",
    }
    errors = []
    # Mock the accounts.get_by method to simulate no existing account
    with app.app_context():
        with patch("api.repositories.accounts.get_by") as mock_get_by:
            mock_get_by.side_effect = NoResultFound()

            # Mock the Account save method to return a dummy account
            with patch.object(Account, "save") as mock_save:
                mock_save.return_value = None

                result = create(data, errors)

    # Verify that the function created a new account
    assert not isinstance(result, Account)
    expected = [
        {"ref": "country", "message": "Length must be between 2 and 2."},
        {"ref": "account_name", "message": "Shorter than minimum length 3."},
        {"ref": "email", "message": "email-invalid"},
    ]

    # Check if it is a subset
    assert expected == errors

    assert len(errors) == 3


def test_create_new_account_with_unknown_field(app):
    data = {"test": "abc"}
    errors = []
    # Mock the accounts.get_by method to simulate no existing account
    with app.app_context():
        with patch("api.repositories.accounts.get_by") as mock_get_by:
            mock_get_by.side_effect = NoResultFound()

            # Mock the Account save method to return a dummy account
            with patch.object(Account, "save") as mock_save:
                mock_save.return_value = None

                result = create(data, errors)

    # Verify that the function created a new account
    assert not isinstance(result, Account)
    assert errors == [{"ref": "test", "message": "Unknown field."}]
    assert len(errors) == 1


def test_create_new_account_with_missing_fields(app):
    data = {"account_name": ""}
    errors = []
    # Mock the accounts.get_by method to simulate no existing account
    with app.app_context():
        with patch("api.repositories.accounts.get_by") as mock_get_by:
            mock_get_by.side_effect = NoResultFound()

            # Mock the Account save method to return a dummy account
            with patch.object(Account, "save") as mock_save:
                mock_save.return_value = None

                result = create(data, errors)

    # Verify that the function created a new account
    assert not isinstance(result, Account)
    assert errors == [
        {"ref": "account_name", "message": "Shorter than minimum length 3."},
    ]
    assert len(errors) == 1
