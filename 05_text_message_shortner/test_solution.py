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
        
        return sys.stdout.getvalue()
    finally:
        sys.stdin = saved_stdin
        sys.stdout = saved_stdout

def test_short_message_no_trimming():
    input_text = "Hey, I'll meet you at the coffee shop for lunch with Sarah.\n"
    
    output = capture_output(input_text)
    
    assert "Original message (59 chars)" in output, "Original message character count is incorrect"
    assert "Shortened message (54 chars)" in output, "Shortened message character count is incorrect"
    assert "Hey, I'll meet you @ the coffee shop 4 lunch w/ Sarah." in output, "Shortened message text doesn't match expected output"
    assert "You saved 5 characters!" in output, "Character savings count is incorrect"

def test_long_message_trimming():
    input_text = "I wanted to let you know that I'll be running late for our meeting this afternoon. There's heavy traffic on the highway and I'm stuck in a jam. I should be there in about 20 minutes. Please start without me and I'll catch up when I arrive. Thanks for your understanding and patience.\n"
    
    output = capture_output(input_text)
    
    assert "..." in output, "Long message not trimmed with '...' at the end"
    
    for line in output.split("\n"):
        if "Shortened message" in line:
            open_par_index = line.find("(")
            chars = line[open_par_index + 1 : line.find(" ", open_par_index)]
            assert int(chars) <= 160, f"Reported character count ({chars}) exceeds 160 limit"
            
            message_part = line.split(": ")[1]
            assert len(message_part) <= 160, f"Actual shortened message length ({len(message_part)}) exceeds 160 limit"
            assert message_part.endswith("..."), "Trimmed message should end with '...'"

def test_exact_length_trimming():
    input_text = "x" * 160 + "\n"
    
    output = capture_output(input_text)
    
    for line in output.split("\n"):
        if "Shortened message" in line:
            assert "..." not in line, "Message exactly at 160 chars should not be trimmed"
            message_part = line.split(": ")[1]
            assert len(message_part) == 160, f"Expected message length 160, got {len(message_part)}"

def test_boundary_trimming():
    input_text = "x" * 161 + "\n"

    output = capture_output(input_text)
    
    for line in output.split("\n"):
        if "Shortened message" in line:
            assert "..." in line, "Message over 160 chars should be trimmed with '...'"
            message_part = line.split(": ")[1]
            assert len(message_part) == 160, f"Trimmed message should be exactly 160 chars, got {len(message_part)}"
            assert message_part.endswith("..."), "Trimmed message should end with '...'"

def test_abbreviation_replacements():
    input_text = "I want to meet with you and talk for a bit at the cafe.\n"
    
    output = capture_output(input_text)
    
    shortened_message = ""
    for line in output.split("\n"):
        if "Shortened message" in line:
            shortened_message = line.split(": ")[1]
            break
    
    assert "2" in shortened_message, "Replacement 'to' → '2' not applied"
    assert "w/" in shortened_message, "Replacement 'with' → 'w/' not applied"
    assert "&" in shortened_message, "Replacement 'and' → '&' not applied"
    assert "4" in shortened_message, "Replacement 'for' → '4' not applied"
    assert "@" in shortened_message, "Replacement 'at' → '@' not applied"
    
    assert "to" not in shortened_message, "Word 'to' still present in shortened message"
    assert "with" not in shortened_message, "Word 'with' still present in shortened message"
    assert "and" not in shortened_message, "Word 'and' still present in shortened message"
    assert "for" not in shortened_message, "Word 'for' still present in shortened message"
    assert "at" not in shortened_message, "Word 'at' still present in shortened message"

def test_capitalization():
    input_text = "hello, this is a test message.\n"
    
    output = capture_output(input_text)
    
    for line in output.split("\n"):
        if "Shortened message" in line:
            message_part = line.split(": ")[1]
            assert message_part[0].isupper(), "First letter of message should be capitalized"
            assert message_part.startswith("Hello"), f"Expected message to start with 'Hello', got '{message_part[:5]}'"

def test_already_capitalized():
    input_text = "Hello, this is already capitalized.\n"
    
    output = capture_output(input_text)
    
    for line in output.split("\n"):
        if "Shortened message" in line:
            message_part = line.split(": ")[1]
            assert message_part[0].isupper(), "First letter of already capitalized message should remain capitalized"
            assert message_part.startswith("Hello"), f"Message should still start with 'Hello', got '{message_part[:5]}'"

def test_character_count_matches():
    input_text = "Testing character count accuracy for both messages.\n"
    
    output = capture_output(input_text)
    
    print("\nDEBUG - Captured output:")
    print(output)
    
    original_reported_length = 0
    shortened_reported_length = 0
    chars_saved = 0
    
    for line in output.split("\n"):
        if "Original message" in line:
            parts = line.split("(")[1].split(" ")[0]
            original_reported_length = int(parts)
            
        if "Shortened message" in line:
            parts = line.split("(")[1].split(" ")[0]
            shortened_reported_length = int(parts)
            
        if "You saved" in line:
            saved = int(line.split("You saved ")[1].split(" ")[0])
            chars_saved = saved
    
    assert chars_saved == original_reported_length - shortened_reported_length, \
        f"Reported saved characters ({chars_saved}) doesn't match expected ({original_reported_length - shortened_reported_length})"
    
    assert len(input_text.strip()) == original_reported_length, \
        f"Input length ({len(input_text.strip())}) doesn't match reported original length ({original_reported_length})"