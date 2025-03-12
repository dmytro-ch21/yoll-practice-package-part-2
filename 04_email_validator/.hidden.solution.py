def main():
    # prompt for email, and trim the input
    email = input("Enter your email: ").strip()

    # Check for spaces first
    if ' ' in email:
        print("Email cannot contain spaces")
        return

    # Check for the presence of an @ symbol
    if "@" not in email:
        print("Email must contain an @ symbol")
        return

    # Check that there is exactly one @ symbol
    if email.count("@") != 1:
        print("Email must contain only one @ symbol")
        return

    # Check that there is at least one character before the @ symbol
    local, domain = email.split("@")
    if local == "":
        print("Email must have characters before the @ symbol")
        return

    # Check that the domain part has a period (.)
    if "." not in domain:
        print("Email must have a domain with a period after the @ symbol")
        return

    # If all checks pass, the email is valid.
    print("Valid email address!")

main()