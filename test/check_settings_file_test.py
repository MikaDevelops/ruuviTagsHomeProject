import unittest
import setup_ble_station.check_settings_file as check
import setup_ble_station.settings_load as load

class TestCheckSettingsFile(unittest.TestCase):
    
    def test_check_file_false_if_file_not_exists(self):
        result = check.file_present('./test/mocksettings-err.json')
        self.assertFalse(result)

    def test_chek_file_true_if_file_exists(self):
        result = check.file_present('./test/mocksettings.json')
        self.assertTrue(result)

    def test_check_setting_file_valid_true(self):
        settings = load.settings_from_file('./test/mocksettings.json')
        result = check.settings_valid(settings)
        self.assertTrue(result)

    def test_check_setting_file_valid_false(self):
        settings = load.settings_from_file('./test/mock_wrong_settings.json')
        result = check.settings_valid(settings)
        self.assertFalse(result)