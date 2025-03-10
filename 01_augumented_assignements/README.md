# 01_augmented_assignment

<span>

## IMPORTANT READ CAREFULLY:
### Before you start:
> The given `solution.py` file where you will write your code has few lines of code. Essentially it has a `main` function that modularizes the code you will write and makes it easier to test. Your job is to write your code inside of that function. To make your code inside of that function use the 4 spaces indentation (IMPORTANT). This is how python understands scopes.
#### Example:
```python
def my_function():
    print("This is part of the function scope")
    print("This as well")

print("This is outside of the function scope")
```
In addition to that you will see this code:
```python
if __name__ == "__main__":
    main()
```
> Since we will import this `file` aka `module` - `solution.py` into another `module` where it will be tested, we need to ensure it will not run automatically on `import`. That's why we set an `if` statement and make sure that when the module to run is named `"__main__"` only then - run it. We will discuss it in the future and you don't really need to change it for now, the explanation is just for your understanding. 

 ### <span style="background-color: #fff9241b; padding: 1rem; border-radius: 4px"> 🚀 Alright! Now you are ready to proceed! 🚀</span>
</span>



## Description
This assignment simulates a simple bank transaction using augmented assignment operators in Python. The program updates an account balance by processing a deposit and a withdrawal. For the withdrawal, a 3% transaction fee is applied. All operations are performed sequentially without using any loops.

## Instructions
0. **Given**
    - You have a variable `balance = 5000` 
    - Also a statement giving a visual signal about Balance 
    `================== BALANCE ====================`
    - And a `Current Balance: $5000` print

1. **Deposit Step:**
   - The user is prompted to enter an amount to deposit.
   `How much do you want to deposit: $`
   - The input is recieved and stored.
   - Next make the needed operation to update the balance with deposit.
   - The new balance is printed in this format:
   `Balance Successfully Updated: $ updated balance` 

3. **Withdrawal Step:**
   - The user is prompted to enter an amount to withdraw.
   `How much do you want to withdraw: $`
   - The input is recieved and stored.
   - The program displays a message indicating a 3% transaction fee.
   `There is a 3% transaction fee on the withdrawal.`
   - The fee is calculated as 3% of the withdrawal amount.
   - The withdrawal amount and fee are printed in this format.
   `Withdrawal: $500 - Fee: $15` - the numbers will be different depending on inputs.
   - The balance is updated by subtracting the withdrawal amount plus the fee.
   - The updated balance is printed.
   `Balance Successfully Updated: $ updated balance` 

4. **Completion Message:**
   - A final message `============ TRANSACTION COMPLETED ============` is printed.

## Expected Output In Terminal:
```text
================== BALANCE ====================

Current Balance: $5000.0
How much do you want to deposit: $1000
Balance Successfully Updated: $6000.0
How much do you want to withdraw: $500
There is a 3% transaction fee on the withdrawal.
Withdrawal: $500 - Fee: $15
Balance Successfully Updated: $5485.0

============ TRANSACTION COMPLETED ============
```

