import pytest
from unittest.mock import patch
import sys
import io

import solution

class TestPhoneFormatter:
    
    ERROR_MESSAGE: str = "Error: Please enter exactly 10 digits.\nNo spaces, special characters and alphabetical characters."
    
    @patch('builtins.input', return_value='1234567890')
    def test_valid_phone_number(self, mock_input, capsys):
        solution.main()
        captured = capsys.readouterr()
        assert "Formatted Phone Number: (123) 456-7890" in captured.out, \
            "Failed to correctly format a valid 10-digit phone number as: (123) 456-7890"
    
    @patch('builtins.input', return_value='9876543210')
    def test_valid_phone_number_different(self, mock_input, capsys):
        solution.main()
        captured = capsys.readouterr()
        assert "Formatted Phone Number: (987) 654-3210" in captured.out, \
            "Failed to correctly format a second valid 10-digit phone number as: (987) 654-3210"
    
    @patch('builtins.input', return_value='12345')
    def test_short_phone_number(self, mock_input, capsys):
        with pytest.raises(SystemExit):
            solution.main()
        
        captured = capsys.readouterr()
        assert self.ERROR_MESSAGE in captured.out, \
            f"Expected: {self.ERROR_MESSAGE}"
    
    @patch('builtins.input', return_value='12345678901')
    def test_long_phone_number(self, mock_input, capsys):
        with pytest.raises(SystemExit):
            solution.main()
        
        captured = capsys.readouterr()
        assert self.ERROR_MESSAGE in captured.out, \
            f"Expected: {self.ERROR_MESSAGE}"
    
    @patch('builtins.input', return_value='123456789a')
    def test_phone_number_with_letter(self, mock_input, capsys):
        with pytest.raises(SystemExit):
            solution.main()
        
        captured = capsys.readouterr()
        assert self.ERROR_MESSAGE in captured.out, \
            "Failed to show error message for number containing letter"
    
    @patch('builtins.input', return_value='123 456 789')
    def test_phone_number_with_spaces(self, mock_input, capsys):
        with pytest.raises(SystemExit):
            solution.main()
        
        captured = capsys.readouterr()
        assert self.ERROR_MESSAGE in captured.out, \
            f"Expected: {self.ERROR_MESSAGE}"
    
    @patch('builtins.input', return_value='123-456-7890')
    def test_phone_number_with_hyphens(self, mock_input, capsys):
        with pytest.raises(SystemExit):
            solution.main()
        
        captured = capsys.readouterr()
        assert self.ERROR_MESSAGE in captured.out, \
            f"Expected: {self.ERROR_MESSAGE}"
    
    @patch('builtins.input', return_value='(123)456-7890')
    def test_phone_number_with_parentheses(self, mock_input, capsys):
        with pytest.raises(SystemExit):
            solution.main()
        
        captured = capsys.readouterr()
        assert self.ERROR_MESSAGE in captured.out, \
            f"Expected: {self.ERROR_MESSAGE}"