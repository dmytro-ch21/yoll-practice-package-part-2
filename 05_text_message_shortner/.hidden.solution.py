def main():
    message = input("Enter a message: ").strip()
    original_length = len(message)
    
    shortened_message = message.replace("with", "w/")
    shortened_message = shortened_message.replace("for", "4")
    shortened_message = shortened_message.replace("to", "2")
    shortened_message = shortened_message.replace("and", "&")
    shortened_message = shortened_message.replace("at", "@")
    
    if len(shortened_message) > 160:
        shortened_message = shortened_message[:157] + "..."
    
    if shortened_message:
        shortened_message = shortened_message[0].upper() +  shortened_message[1:]
    
    shortened_length = len(shortened_message)
        
    print(f"Original message ({original_length} chars): {message}")    
    print(f"Shortened message ({len(shortened_message)} chars): {shortened_message}")
    print(f"You saved {original_length - shortened_length} characters!")    
    
main()