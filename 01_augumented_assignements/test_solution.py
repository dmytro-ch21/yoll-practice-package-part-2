import pytest
from solution import main

def test_main(capsys, monkeypatch):
    inputs = iter(["1000", "500"])
    

    def fake_input(prompt):
        print(prompt, end="")
        value = next(inputs)
        print(value)
        return value
    
    monkeypatch.setattr("builtins.input", fake_input)
    
    main()
    
    captured_lines = capsys.readouterr().out.splitlines()
    
    expected_lines = [
        "================== BALANCE ====================",
        "",
        "Current Balance: $5000.0",
        "How much do you want to deposit: $1000",
        "Balance Successfully Updated: $6000.0",
        "How much do you want to withdraw: $500",
        "There is a 3% transaction fee on the withdrawal.",
        "Withdrawal: $500.0 - Fee: $15.0",
        "Balance Successfully Updated: $5485.0",
        "",
        "============ TRANSACTION COMPLETED ============"
    ]
    
    for idx, expected in enumerate(expected_lines):
        assert captured_lines[idx] == expected, (
            f"Line {idx+1} expected: '{expected}', got: '{captured_lines[idx]}'"
        )