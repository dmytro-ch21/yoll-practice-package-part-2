import pytest
from unittest.mock import patch
import sys
import io

import solution

class TestPhoneFormatter:
    """Test suite for phone number formatter application."""

    @patch('builtins.input', return_value='1234567890')
    def test_valid_phone_number(self, mock_input, capsys):
        """
        Test with a valid 10-digit phone number.
        Should format and print the number correctly.
        """
        solution.main()
        captured = capsys.readouterr()
        assert "Formatted Phone Number: (123) 456-7890" in captured.out, \
            "Failed to correctly format a valid 10-digit phone number"
    
    @patch('builtins.input', return_value='9876543210')
    def test_valid_phone_number_different(self, mock_input, capsys):
        """
        Test with another valid 10-digit phone number.
        Should format and print the number correctly.
        """
        solution.main()
        captured = capsys.readouterr()
        assert "Formatted Phone Number: (987) 654-3210" in captured.out, \
            "Failed to correctly format a second valid 10-digit phone number"
    
    @patch('builtins.input', return_value='12345')
    def test_short_phone_number(self, mock_input, capsys):
        """
        Test with a phone number shorter than 10 digits.
        Should display an error message and exit.
        """
        with pytest.raises(SystemExit):
            solution.main()
        
        captured = capsys.readouterr()
        assert "Error: Please enter exactly 10 digits" in captured.out, \
            "Failed to show error message for short phone number"
    
    @patch('builtins.input', return_value='12345678901')
    def test_long_phone_number(self, mock_input, capsys):
        """
        Test with a phone number longer than 10 digits.
        Should display an error message and exit.
        """
        with pytest.raises(SystemExit):
            solution.main()
        
        captured = capsys.readouterr()
        assert "Error: Please enter exactly 10 digits" in captured.out, \
            "Failed to show error message for long phone number"
    
    @patch('builtins.input', return_value='123456789a')
    def test_phone_number_with_letter(self, mock_input, capsys):
        """
        Test with a phone number containing a letter.
        Should display an error message and exit.
        """
        with pytest.raises(SystemExit):
            solution.main()
        
        captured = capsys.readouterr()
        assert "Error: Please enter exactly 10 digits" in captured.out, \
            "Failed to show error message for number containing letter"
    
    @patch('builtins.input', return_value='123 456 789')
    def test_phone_number_with_spaces(self, mock_input, capsys):
        """
        Test with a phone number containing spaces.
        Should display an error message and exit.
        """
        with pytest.raises(SystemExit):
            solution.main()
        
        captured = capsys.readouterr()
        assert "Error: Please enter exactly 10 digits" in captured.out, \
            "Failed to show error message for number containing spaces"
    
    @patch('builtins.input', return_value='123-456-7890')
    def test_phone_number_with_hyphens(self, mock_input, capsys):
        """
        Test with a phone number containing hyphens.
        Should display an error message and exit.
        """
        with pytest.raises(SystemExit):
            solution.main()
        
        captured = capsys.readouterr()
        assert "Error: Please enter exactly 10 digits" in captured.out, \
            "Failed to show error message for number containing hyphens"
    
    @patch('builtins.input', return_value='(123)456-7890')
    def test_phone_number_with_parentheses(self, mock_input, capsys):
        """
        Test with a phone number containing parentheses.
        Should display an error message and exit.
        """
        with pytest.raises(SystemExit):
            solution.main()
        
        captured = capsys.readouterr()
        assert "Error: Please enter exactly 10 digits" in captured.out, \
            "Failed to show error message for number containing parentheses"