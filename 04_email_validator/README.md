# 04_email_validator

## Description
In this exercise, you are tasked to create the logic that will validate an email address. A valid email must satisfy the following conditions:
- Contains exactly one `@` symbol
- Has at least one character before the `@` symbol
- Has a domain name after the `@` with at least one period (.)
- Contains no spaces

## Instructions
1. Prompt the user to enter an email address
2. Check if the email satisfies all the conditions for validity
3. If the email is valid, output "Valid email address!"
4. If the email is invalid, output a specific message indicating the issue:
   - "Email must contain an @ symbol" if there is no @ symbol
   - "Email must contain only one @ symbol" if there are multiple @ symbols
   - "Email must have characters before the @ symbol" if there are no characters before @
   - "Email must have a domain with a period after the @ symbol" if there is no period after the @
   - "Email cannot contain spaces" if there are any spaces

## Expected Output

### Valid Email:
```
Enter an email address: user.name@example.com
Valid email address!
```

### Invalid Email (No @ symbol):
```
Enter an email address: username.example.com
Email must contain an @ symbol
```

### Invalid Email (Multiple @ symbols):
```
Enter an email address: user@name@example.com
Email must contain only one @ symbol
```

### Invalid Email (No characters before @):
```
Enter an email address: @example.com
Email must have characters before the @ symbol
```

### Invalid Email (No period in domain):
```
Enter an email address: username@examplecom
Email must have a domain with a period after the @ symbol
```

### Invalid Email (Contains spaces):
```
Enter an email address: user name@example.com
Email cannot contain spaces
```

## Hints
- Use the `.count()` method to check how many times a character appears in a string
- Use the `.find()` method to get the position of a character in a string
- Use the `in` operator to check if a character exists in a string