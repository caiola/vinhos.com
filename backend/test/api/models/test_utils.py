import unittest

from api.models.utils import get_value


class GetValueTestCase(unittest.TestCase):
    def test_get_value_with_valid_key(self):
        data = {'key': 'value'}
        key = 'key'
        default = 'default'
        result = get_value(data, key, default)
        self.assertEqual(result, 'value')

    def test_get_value_with_invalid_key(self):
        data = {'key': 'value'}
        key = 'invalid_key'
        default = 'default'
        result = get_value(data, key, default)
        self.assertEqual(result, 'default')

    def test_get_value_with_none_data(self):
        data = None
        key = 'key'
        default = 'default'
        result = get_value(data, key, default)
        self.assertEqual(result, 'default')

    def test_get_value_with_attribute_error(self):
        data = object()
        key = 'key'
        default = 'default'
        result = get_value(data, key, default)
        self.assertEqual(result, 'default')

    def test_get_value_with_type_error(self):
        data = 123
        key = 'key'
        default = 'default'
        result = get_value(data, key, default)
        self.assertEqual(result, 'default')

# if __name__ == '__main__':
#     unittest.main()
