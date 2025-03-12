# 02_phone_number_formatter

## Description
This exercise formats a raw 10-digit phone number into a standard U.S. format: `(123) 456-7890`. It practices string slicing and formatting.

## Instructions
1. Prompt the user to enter a 10-digit phone number as below:
    ```text 
    Enter a 10-digit phone number, no spaces, special characters or spaces:
    ```
2. Validate that the input contains exactly 10 digits. If not, display an error message and exit the program.
    ```text
    Error: Please enter exactly 10 digits.
    No spaces, special characters and alphabetical characters.
    ```
   
3. Use string slicing to extract the area code, first three digits, and last four digits.
4. Format these parts into the standard format: `(123) 456-7890`.
5. Print the formatted phone number.

## Expected Output In Terminal
##### Happy Path:
```text
Enter a 10-digit phone number: 1234567890
Formatted Phone Number: (123) 456-7890
```

##### Nagative Test: Number shorter than 10 digits
```text
Enter a 10-digit phone number: 12321
Error: Please enter exactly 10 digits.
No spaces, special characters and alphabetical characters.
```

##### Nagative Test: Number contains letters, spaces or special characters
```text
Enter a 10-digit phone number: 123321121a
Error: Please enter exactly 10 digits.
No spaces, special characters and alphabetical characters.
```

> #### 😉 Hints:
    >> ---
    >> 1. You do not need `if` statements to control the flow.Remember you have the logical operators `and` `or` short circuits. You can control if the error message is printed based on a condition, `if length matches a certain number`. If the result is `true` do not evaluate second operator, if condition is false evaluate second operand.
    >>
    >> **Example**
    >> ```python
    >>    is_real = False
    >>    is_real or print("Error") # here if is_real is true print will not evaluate, otherwise it will
    >> ```
    >> ---
    >> 2. In addition you can termiante a program in different way, in this situation you can use `exit()` function. 
    >> ---
        