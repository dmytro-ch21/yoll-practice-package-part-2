def main():
    balance = 5000.0

    print("================== BALANCE ====================")
    print("")
    print(f"Current Balance: ${balance}")
    
    # Deposit step
    deposit = float(input("How much do you want to deposit: $"))
    balance += deposit
    print(f"Balance Successfully Updated: ${balance}")
    
    # Withdrawal step
    withdrawal = float(input("How much do you want to withdraw: $"))
    print("There is a 3% transaction fee on the withdrawal.")
    
    # Calculate fee
    fee = withdrawal * 0.03
    print(f"Withdrawal: ${withdrawal} - Fee: ${fee}")
    
    # Update balance with withdrawal and fee
    balance -= withdrawal + fee
    print(f"Balance Successfully Updated: ${balance}")
    
    # Completion message
    print("")
    print("============ TRANSACTION COMPLETED ============")

if __name__ == "__main__":
    main()    