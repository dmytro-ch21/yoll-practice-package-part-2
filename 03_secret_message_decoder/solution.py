# do not change the method name
def main():
    
    encoded_message = input("Enter the encoded message: ")
    step_input = input("Enter the step size: ")
    
    is_valid_step = step_input.isdigit() and int(step_input) > 0
    is_valid_step or print("Error: Step size must be a positive integer.")
    is_valid_step or exit()
    
    step = int(step_input)
    
    decoded_message = encoded_message[::step]
    
    print(f"Decoded Message: {decoded_message}")

# do not change the following lines:    
if __name__ == "__main__":
    main()