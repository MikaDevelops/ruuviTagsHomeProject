import unittest
import setup_ble_station.cli_wizard_checks as check

class TestCliWizardChecks(unittest.TestCase):

    def test_directory_valid_false_if_space(self):
        result = check.directory_valid('some  directory')
        self.assertFalse(result)

    def test_directory_valid_false_if_empty(self):
        result = check.directory_valid('')
        self.assertFalse(result)

    def test_directory_valid_false_if_special(self):
        result = check.directory_valid('ö')
        self.assertFalse(result)

    def test_directory_exists_returns_false_when_no_dir_found(self):
        result = check.directory_exists('dsjhfwofhdishsd78s7323no23vuhw')
        self.assertFalse(result)