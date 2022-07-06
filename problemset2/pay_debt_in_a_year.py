'''
	      # Test Case 1:
	      balance = 42
	      annualInterestRate = 0.2
	      monthlyPaymentRate = 0.04
	      
	      # Result Your Code Should Generate Below:
	      Remaining balance: 31.38
                    
          # To make sure you are doing calculation correctly, this is the 
          # remaining balance you should be getting at each month for this example
            Month 1 Remaining balance: 40.99
            Month 2 Remaining balance: 40.01
            Month 3 Remaining balance: 39.05
            Month 4 Remaining balance: 38.11
            Month 5 Remaining balance: 37.2
            Month 6 Remaining balance: 36.3
            Month 7 Remaining balance: 35.43
            Month 8 Remaining balance: 34.58
            Month 9 Remaining balance: 33.75
            Month 10 Remaining balance: 32.94
            Month 11 Remaining balance: 32.15
            Month 12 Remaining balance: 31.38

                


	      Test Case 2:
	      balance = 484
	      annualInterestRate = 0.2
	      monthlyPaymentRate = 0.04
	      
	      Result Your Code Should Generate Below:
	      Remaining balance: 361.61
'''
balance = 484
annualInterestRate = 0.2
monthlyPaymentRate = 0.04
'''
Function to calculate the balance on a credit card that remains after one year of paying it off
'''
def remainingBalance(balance, annualInterestRate, monthlyPaymentRate):
    months = 12
    monthlyInterestRate = annualInterestRate / 12.0
    minimumMonthlyPayment = 0
    monthlyUnpaidBalance = 0
    for i in range(months+1):
        if i == 0:
            remaining_balance = balance
        else:
            minimumMonthlyPayment = monthlyPaymentRate*remaining_balance
            monthlyUnpaidBalance = remaining_balance - minimumMonthlyPayment
            remaining_balance = monthlyUnpaidBalance + monthlyInterestRate*monthlyUnpaidBalance
            print("Month "+ str(i) + " Remaining balance: " + str(round(remaining_balance,2)))
    print("Remaining balance: " + str(round(remaining_balance,2)))
remainingBalance(balance, annualInterestRate, monthlyPaymentRate)