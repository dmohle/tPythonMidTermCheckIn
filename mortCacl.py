# Hard-code the interest rate, original loan balance, original monthly amount due, and monthly escrow
interest_rate = 0.0275
original_loan_balance = 323216.46
original_monthly_amount_due = 2019.34
monthly_escrow = 463.05

# Prompt the user for the monthly extra payment
monthly_extra_payment = int(input("Enter the monthly extra payment: "))

# Calculate the monthly loan payment
monthly_loan_payment = original_monthly_amount_due - monthly_escrow

# Add the monthly extra payment to the monthly loan payment
monthly_loan_payment += monthly_extra_payment
print(f"\n\nmonthly loan payment is: {monthly_loan_payment}\n\n")
# Initialize the loan balance
loan_balance = original_loan_balance
print(f"loan_balance is: {loan_balance}")

# Create a list to store the loan balance for each year
loan_balance_by_year = []

# Calculate the loan balance for each year


for year in range(1, 31):
    # Calculate the annual interest.
    yearly_interest = loan_balance * interest_rate
    print(f"yearly interest is: {yearly_interest}\n")

    # Interest and principal.
    int_and_principal = loan_balance + yearly_interest
    print(f"int and principal is: {int_and_principal}\n")

    loan_balance = int_and_principal - (12 * monthly_loan_payment)
    print(f"loan balance is: {loan_balance}\n")
    print(f"monthly loan payment is: {monthly_loan_payment}")

    # Add the loan balance for the year to the list
    loan_balance_by_year.append(loan_balance)

# Print the loan balance for each year
for year, loan_balance in enumerate(loan_balance_by_year):
    print("Year {}: ${:.2f}".format(year + 1, loan_balance))