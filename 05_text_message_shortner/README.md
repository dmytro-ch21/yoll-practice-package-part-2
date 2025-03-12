# 05_text_message_shortener

## Description
In this exercise, you will create a program that shortens a text message to fit within SMS character limits (160 characters). The shortening process should follow specific rules to maintain readability while reducing the message length.

## Instructions
1. Prompt the user to enter a text message
2. Shorten the message using the following rules:
   - Replace common words with abbreviations:
     * `with` → `w/`
     * `for` → `4`
     * `to` → `2`
     * `and` → `&`
     * `at` → `@`
   - If the message is longer than 160 characters, trim it and add "`...`" at the end
   - Make sure the first letter of the message is capitalized
3. Display both the original message and the shortened message
4. Show the character count for both messages and how many characters were saved

## Expected Output

### Short Message (no trimming needed):
```
Enter a message: Hey, I'll meet you at the coffee shop for lunch with Sarah.
Original message (59 chars): Hey, I'll meet you at the coffee shop for lunch with Sarah.
Shortened message (54 chars): Hey, I'll meet you @ the coffee shop 4 lunch w/ Sarah.
You saved 5 characters!
```

### Long Message (trimming needed):
```
Enter a message: I wanted to let you know that I'll be running late for our meeting this afternoon. There's heavy traffic on the highway and I'm stuck in a jam. I should be there in about 20 minutes. Please start without me and I'll catch up when I arrive. Thanks for your understanding and patience.
Original message (283 chars): I wanted to let you know that I'll be running late for our meeting this afternoon. There's heavy traffic on the highway and I'm stuck in a jam. I should be there in about 20 minutes. Please start without me and I'll catch up when I arrive. Thanks for your understanding and patience.
Shortened message (160 chars): I wanted 2 let you know th@ I'll be running l@e 4 our meeting this afternoon. There's heavy traffic on the highway & I'm stuck in a jam. I should be there in...
You saved 123 characters!
```

## Hints
- Use the `.replace()` method to substitute words with abbreviations
- Use string slicing to trim the message if it's too long (`message[:157] + "..."`)
- Use the `len()` function to get the length of a string
- Remember to capitalize the first letter after all other operations are complete