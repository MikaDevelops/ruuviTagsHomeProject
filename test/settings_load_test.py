import json
import unittest
import setup_ble_station.settings_load as load

class TestSettingsLoad(unittest.TestCase):

    def test_returns_dictionary(self):
        settings_file = './test/mocksettings.json'
        result = load.settings_from_file(settings_file)
        is_dictionary = isinstance(result,dict)
        self.assertTrue(is_dictionary)

    def test_raises_error_on_not_valid_json(self):
        settings_file = './test/mock_invalid.json'
        with self.assertRaises(json.JSONDecodeError):
            load.settings_from_file(settings_file)