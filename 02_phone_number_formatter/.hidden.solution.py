def main():
    # Prompt user for input
    phone_number = input("Enter a 10-digit phone number: ")
    
    # Validate input that must be exactly 10 digits
    is_valid = (len(phone_number) == 10 and phone_number.isdigit())
    
    # If invalid print error and exit
    is_valid or print("Error: Please enter exactly 10 digits.\nNo spaces, special characters and alphabetical characters.") or exit()
    
    # Extract parts using string slicing
    area_code = phone_number[:3]
    first_part = phone_number[3:6]
    second_part = phone_number[6:]
    
    # Format and print the phone number
    formatted_number = f"({area_code}) {first_part}-{second_part}"
    print(f"Formatted Phone Number: {formatted_number}")

if __name__ == "__main__":
    main()