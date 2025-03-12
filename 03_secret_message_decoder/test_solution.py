import pytest
from unittest.mock import patch
import io
import sys

import solution

class TestSecretMessageDecoder:

    @patch('builtins.input', side_effect=['HH17GekrZblLSrvlxRpWoo[Df C*WrWZb>CoKp=&r(kpul1$7Sd:t6r!C4Lc', '5'])
    def test_hello_world_message(self, mock_input, capsys):
        solution.main()
        captured = capsys.readouterr()
        assert "Decoded Message: Hello World!" in captured.out, \
            "Failed to correctly decode hidden greeting with step size 5"
    
    @patch('builtins.input', side_effect=['BNb1e1bIlF2tix)Gei~*v0BNe=!N }{Ii2RqnU]t tnPybRhoLH6uWi2rK:?sezXemeslvC[f3,}.^)V', '4'])
    def test_inspiration_message(self, mock_input, capsys):
        solution.main()
        captured = capsys.readouterr()
        assert "Decoded Message: Believe in yourself." in captured.out, \
            "Failed to correctly decode hidden quote with step size 4"
    
    @patch('builtins.input', side_effect=['Wf=hEBa52t~@ -[gL(ek:tQas6C $HwHieM[tNHt6ee%;rrc jLa2ksvg N}iC2t@j yvdRBrc7i?)eq3sp}?xf', '3'])
    def test_riddle(self, mock_input, capsys):
        solution.main()
        captured = capsys.readouterr()
        assert "Decoded Message: What gets wetter as it dries?" in captured.out, \
            "Failed to correctly decode hidden riddle with step size 3"
    
    @patch('builtins.input', side_effect=['Tza likJ ?iFsQ :c?hxeJaMp-.} sSWhwo4wP Ympe! _t3hMe} Nc.o;die@.& 9—U ALIi9n0uGsn 9Tmonrtv]a ludGs,', '2'])
    def test_secret_password(self, mock_input, capsys):
        solution.main()
        captured = capsys.readouterr()
        assert "Decoded Message: Talk is cheap. Show me the code. — Linus Torvalds" in captured.out, \
            "Failed to correctly decode secret password with step size 2"
    
    @patch('builtins.input', side_effect=['XYZ', '1'])
    def test_step_size_one(self, mock_input, capsys):
        solution.main()
        captured = capsys.readouterr()
        assert "Decoded Message: XYZ" in captured.out, \
            "Failed to correctly decode with step size 1"
    
    @patch('builtins.input', side_effect=['ABCDEFG', '2'])
    def test_every_second_character(self, mock_input, capsys):
        solution.main()
        captured = capsys.readouterr()
        assert "Decoded Message: ACE" in captured.out, \
            "Failed to correctly decode every second character"
    
    @patch('builtins.input', side_effect=['', '3'])
    def test_empty_message(self, mock_input, capsys):

        solution.main()
        captured = capsys.readouterr()
        assert "Decoded Message: " in captured.out, \
            "Failed to handle an empty message correctly"
    
    @patch('builtins.input', side_effect=['Hello', 'abc'])
    def test_invalid_step_non_numeric(self, mock_input, capsys):
        with pytest.raises(SystemExit):
            solution.main()
        
        captured = capsys.readouterr()
        assert "Error: Step size must be a positive integer" in captured.out, \
            "Failed to show error message for non-numeric step"
    
    @patch('builtins.input', side_effect=['Hello', '0'])
    def test_invalid_step_zero(self, mock_input, capsys):
        with pytest.raises(SystemExit):
            solution.main()
        
        captured = capsys.readouterr()
        assert "Error: Step size must be a positive integer" in captured.out, \
            "Failed to show error message for zero step"
    
    @patch('builtins.input', side_effect=['Hello', '-5'])
    def test_invalid_step_negative(self, mock_input, capsys):
        with pytest.raises(SystemExit):
            solution.main()
        
        captured = capsys.readouterr()
        assert "Error: Step size must be a positive integer" in captured.out, \
            "Failed to show error message for negative step"