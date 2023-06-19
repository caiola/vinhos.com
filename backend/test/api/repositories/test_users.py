from unittest.mock import patch

import pytest
from marshmallow import ValidationError
from sqlalchemy.exc import NoResultFound

from api.models import User
from api.repositories import users
from api.repositories.users import UserCreateSchema, create, exists, get_by


# @TODO FIX get by pk
# def test_get_by_with_pk():
#     user = User(pk=1, uuid="123", email="test@example.com")
#     with patch.object(users.User, "query") as mock_query:
#         mock_query.filter_by.return_value.one.return_value = user
#         result = get_by(pk=1)
#     assert result == user
#
# @TODO FIX get by uuid
#
# def test_get_by_with_uuid():
#     user = User(pk=1, uuid="123", email="test@example.com")
#     with patch.object(users.User, "query") as mock_query:
#         mock_query.filter_by.return_value.one.return_value = user
#         result = get_by(uuid="123")
#     assert result == user
#
#
def test_get_by_with_email(app):
    user = User(email="test@example.com")
    with app.app_context():
        with patch.object(users.User, "query") as mock_query:
            mock_query.filter_by.return_value.one.return_value = user
            result = get_by(email="test@example.com")
    assert result == user


# @TODO Raise error when parameters are not set properly
# def test_get_by_with_invalid_params(app):
#     with app.app_context():
#         with pytest.raises(ValueError):
#             get_by()
#
# @TODO FIX update method => RuntimeError: The current Flask app is not registered with this "SQLAlchemy" instance.
# def test_update(app):
#     user = User(email="test@example.com")
#     with app.app_context():
#         with patch.object(users.User, "update") as mock_update:
#             mock_update.return_value = user
#             result = update(user, email="new@example.com")
#     assert result == user


def test_exists_with_existing_email(app):
    data = {"email": "test@example.com"}
    errors = []
    user = User(email="test@example.com")
    with app.app_context():
        with patch.object(users, "get_by") as mock_get_by:
            mock_get_by.return_value = user
            result = exists(data, errors)
    assert result is True
    assert errors == [{"ref": "user", "message": "Email already exists"}]


def test_exists_with_non_existing_email(app):
    data = {"email": "test@example.com"}
    errors = []
    with app.app_context():
        with patch.object(users, "get_by") as mock_get_by:
            mock_get_by.return_value = None
            result = exists(data, errors)
    assert result is False
    assert errors == []


def test_exists_with_value_error(app):
    data = {"email": "test@example.com"}
    errors = []
    with app.app_context():
        with patch("api.repositories.users.get_by") as mock_get_by:
            mock_get_by.side_effect = ValueError("Custom error message")
            result = exists(data, errors)

    assert result is False
    assert errors == [{"ref": "user", "message": "Custom error message"}]


def test_exists_with_value_no_result_found(app):
    data = {"email": "test@example.com"}
    errors = []
    with app.app_context():
        with patch("api.repositories.users.get_by") as mock_get_by:
            mock_get_by.side_effect = NoResultFound()
            result = exists(data, errors)

    assert result is False
    assert errors == []


def test_create_with_valid_data(app):
    data = {"account_id": 1, "email": "test@example.com"}
    errors = []
    user = User(email="test@example.com")
    with app.app_context():
        with patch.object(UserCreateSchema, "load"):
            with patch.object(users, "get_value") as mock_get_value:
                mock_get_value.return_value = 1
                with patch.object(User, "__init__") as mock_init:
                    mock_init.return_value = None
                    with patch.object(User, "save") as mock_save:
                        mock_save.return_value = user
                        result = create(data, errors)
    assert result == user
    assert errors == []


def test_create_with_invalid_data(app):
    data = {}
    errors = []
    with app.app_context():
        with patch.object(UserCreateSchema, "load") as mock_load:
            mock_load.side_effect = ValidationError(
                {
                    "account_id": ["Missing data for required field."],
                    "email": ["email-required"],
                }
            )
            result = create(data, errors)
    assert result is None
    assert len(errors) > 0
    assert errors == [
        {"ref": "account_id", "message": "Missing data for required field."},
        {"ref": "email", "message": "email-required"},
    ]

    def test_create_with_invalid_account_id(app):
        data = {"email": "test@example.com"}  # Missing required "account_id" field
        errors = []
        with app.app_context():
            with patch.object(UserCreateSchema, "load") as mock_load:
                mock_load.side_effect = ValidationError(
                    {"account_id": ["Missing data for required field."]}
                )
                result = create(data, errors)
        assert result is None
        assert len(errors) > 0
        assert errors == [
            {"ref": "account_id", "message": "Missing data for required field."},
        ]

    def test_create_with_invalid_email(app):
        data = {"account_id": 123}  # Missing required "email" field
        errors = []
        with app.app_context():
            with patch.object(UserCreateSchema, "load") as mock_load:
                mock_load.side_effect = ValidationError({"email": ["email-required"]})
                result = create(data, errors)
        assert result is None
        assert len(errors) > 0
        assert errors == [
            {"ref": "email", "message": "email-required"},
        ]

    def test_create_with_invalid_data_and_unknown_fields(app):
        data = {"xyz_account_id": 123, "abc_email": "test@example.com"}
        errors = []
        with app.app_context():
            with patch.object(UserCreateSchema, "load") as mock_load:
                mock_load.side_effect = ValidationError(
                    {
                        "account_id": ["Missing data for required field."],
                        "email": ["email-required"],
                        "xyz_account_id": ["Unknown field."],
                        "abc_email": ["Unknown field."],
                    }
                )
                result = create(data, errors)
        assert result is None
        assert len(errors) > 0
        assert errors == [
            {"ref": "account_id", "message": "Missing data for required field."},
            {"ref": "email", "message": "email-required"},
            {"ref": "xyz_account_id", "message": "Unknown field."},
            {"ref": "abc_email", "message": "Unknown field."},
        ]
