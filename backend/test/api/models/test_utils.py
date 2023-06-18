import unittest

from api.models.utils import add_error, get_value


class GetValueTestCase(unittest.TestCase):
    def test_get_value_with_valid_key(self):
        data = {"key": "value"}
        key = "key"
        default = "default"
        result = get_value(data, key, default)
        self.assertEqual(result, "value")

    def test_get_value_with_invalid_key(self):
        data = {"key": "value"}
        key = "invalid_key"
        default = "default"
        result = get_value(data, key, default)
        self.assertEqual(result, "default")

    def test_get_value_with_none_data(self):
        data = None
        key = "key"
        default = "default"
        result = get_value(data, key, default)
        self.assertEqual(result, "default")

    def test_get_value_with_attribute_error(self):
        data = object()
        key = "key"
        default = "default"
        result = get_value(data, key, default)
        self.assertEqual(result, "default")

    def test_get_value_with_type_error(self):
        data = 123
        key = "key"
        default = "default"
        result = get_value(data, key, default)
        self.assertEqual(result, "default")


class AddErrorTestCase(unittest.TestCase):
    def test_add_error_empty_list(self):
        errors = []
        key = "ref"
        message = "Error message"
        add_error(errors, key, message)
        assert errors == [{"ref": "ref", "message": "Error message"}]

    def test_add_error_existing_list(self):
        errors = [{"ref": "key1", "message": "Error 1"}]
        key = "key2"
        message = "Error 2"
        add_error(errors, key, message)
        assert errors == [
            {"ref": "key1", "message": "Error 1"},
            {"ref": "key2", "message": "Error 2"},
        ]

    def test_add_error_empty_key(self):
        errors = []
        key = ""
        message = "Error message"
        add_error(errors, key, message)
        assert errors == []

    def test_add_error_empty_message(self):
        errors = []
        key = "ref"
        message = ""
        add_error(errors, key, message)
        assert errors == []

    def test_add_error_special_characters(self):
        errors = []
        key = "@#$%"
        message = "Error #$%"
        add_error(errors, key, message)
        assert errors == [{"ref": "@#$%", "message": "Error #$%"}]

    def test_add_error_unicode_characters(self):
        errors = []
        key = "réf"
        message = "Érrør mèssàgè"
        add_error(errors, key, message)
        assert errors == [{"ref": "réf", "message": "Érrør mèssàgè"}]

    def test_add_error_integer_key_message(self):
        errors = []
        key = 123
        message = 456
        add_error(errors, key, message)
        assert errors == []

    def test_add_error_string_integer_key_message(self):
        errors = []
        key = "123"
        message = 456
        add_error(errors, key, message)
        assert errors == [{"ref": "123", "message": 456}]

    def test_add_error_none_listself(self):
        errors = None
        key = "ref"
        message = "Error message"
        add_error(errors, key, message)
        assert errors is None

    def test_add_error_none_key_message(self):
        errors = []
        key = None
        message = None
        add_error(errors, key, message)
        assert errors == []

    def test_add_error_long_strings(self):
        errors = []
        key = "a" * 1000
        message = "b" * 2000
        add_error(errors, key, message)
        assert errors == [{"ref": "a" * 1000, "message": "b" * 2000}]

    def test_add_error_duplicate_key(self):
        errors = [
            {"ref": "key1", "message": "Error 1"},
            {"ref": "key1", "message": "Error 2"},
        ]
        key = "key1"
        message = "Error 3"
        add_error(errors, key, message)
        assert errors == [
            {"ref": "key1", "message": "Error 1"},
            {"ref": "key1", "message": "Error 2"},
            {"ref": "key1", "message": "Error 3"},
        ]

    def test_add_error_boolean_key_message(self):
        errors = []
        key = True
        message = False
        add_error(errors, key, message)
        assert errors == []

    def test_add_error_boolean_key_message_on_existing_list(self):
        errors = [{"ref": "key1", "message": "Error 1"}]
        key = True
        message = "Msg"
        add_error(errors, key, message)
        assert errors == [
            {"ref": "key1", "message": "Error 1"},
        ]

    def test_add_error_complex_key(self):
        class KeyObject:
            def __init__(self, value):
                self.value = value

        errors = []
        key = KeyObject("ref")
        message = "Error message"
        add_error(errors, key, message)
        assert errors == []

    def test_add_error_same_list_reference(self):
        errors = []
        key = "ref"
        message = "Error message"
        result = add_error(errors, key, message)
        assert result is None

    def test_add_error_float_key_message(self):
        errors = []
        key = 1.23
        message = 4.56
        add_error(errors, key, message)
        assert errors == []

    def test_add_error_str_float_key_message(self):
        errors = []
        key = "1.23"
        message = 4.56
        add_error(errors, key, message)
        assert errors == [{"ref": "1.23", "message": 4.56}]
