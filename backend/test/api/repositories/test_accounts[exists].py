from unittest.mock import patch, MagicMock

from sqlalchemy.exc import NoResultFound

from api.repositories.accounts import exists


@patch("api.repositories.accounts.get_by")
@patch("api.models.utils.add_error")
@patch("api.models.utils.get_value", return_value="existing_account")
def test_exists_account_found(mock_get_value, mock_add_error, mock_get_by):
    mock_get_by.return_value = MagicMock()  # Simulate finding an account
    errors = []
    data = {"account_name": "existing_account"}

    result = exists(data, errors)

    assert result is True
    assert [{'message': 'Account name already exists', 'ref': 'account'}] == errors


@patch("api.repositories.accounts.get_by", side_effect=NoResultFound)
@patch("api.models.utils.add_error")
@patch("api.models.utils.get_value", return_value="non_existing_account")
def test_exists_account_not_found(mock_get_value, mock_add_error, mock_get_by):
    errors = []
    data = {"account_name": "non_existing_account"}

    result = exists(data, errors)

    assert result is False
    mock_add_error.assert_not_called()
    assert [] == errors


@patch("api.repositories.accounts.get_by")
@patch("api.models.utils.add_error")
@patch("api.models.utils.get_value", return_value="existing_account")
def test_exists_account_found_and_keep_existing_errors(mock_get_value, mock_add_error, mock_get_by):
    mock_get_by.return_value = MagicMock()  # Simulate finding an account
    errors = [{'message': 'My existing error', 'ref': 'my-reference'}]
    data = {"account_name": "existing_account"}

    result = exists(data, errors)

    assert result is True
    assert [
               {'message': 'My existing error', 'ref': 'my-reference'},
               {'message': 'Account name already exists', 'ref': 'account'}
           ] == errors
