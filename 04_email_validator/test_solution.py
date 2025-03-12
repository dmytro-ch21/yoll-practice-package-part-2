import pytest
import sys
from io import StringIO

def capture_output(input_value):
    saved_stdin = sys.stdin
    saved_stdout = sys.stdout
    try:
        sys.stdin = StringIO(input_value)
        sys.stdout = StringIO()
        exec(open("solution.py").read())
        return sys.stdout.getvalue().strip()
    finally:
        sys.stdin = saved_stdin
        sys.stdout = saved_stdout

def test_valid_email():
    output = capture_output("user.name@example.com\n")
    assert "Valid email address!" in output

def test_no_at_symbol():
    output = capture_output("username.example.com\n")
    assert "Email must contain an @ symbol" in output

def test_multiple_at_symbols():
    output = capture_output("user@name@example.com\n")
    assert "Email must contain only one @ symbol" in output

def test_no_characters_before_at():
    output = capture_output("@example.com\n")
    assert "Email must have characters before the @ symbol" in output

def test_no_period_in_domain():
    output = capture_output("username@examplecom\n")
    assert "Email must have a domain with a period after the @ symbol" in output

def test_with_spaces():
    output = capture_output("user name@example.com\n")
    assert "Email cannot contain spaces" in output