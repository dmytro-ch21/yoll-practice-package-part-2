# do not change the method name
def main():
    # prompt for message
    encoded_message = input("Enter the encoded message: ")
    # prompt for step
    step_input = input("Enter the step size: ")
    # check if valid - if digit and if valid step more than 0
    is_valid_step = step_input.isdigit() and int(step_input) > 0
    # check if valid step and, if not or operator will evaluate/execute print message
    is_valid_step or print("Error: Step size must be a positive integer.")
    # and exit the program
    is_valid_step or exit()
    # cast step to a int
    step = int(step_input)
    # get decoded message by using the step in slicing
    decoded_message = encoded_message[::step]
    # output the message
    print(f"Decoded Message: {decoded_message}")
if __name__ == "__main__":
    main()